from string import Template

import openai
import requests
from openai.embeddings_utils import get_embedding

from src.open_ai.libs import printing


def config_openai(config: dict) -> None:
    openai.api_type = config["OPENAI_API_TYPE"]
    openai.api_base = config["OPENAI_API_BASE_URL"]
    openai.api_version = config["OPENAI_API_VERSION"]
    openai.api_key = config["OPENAI_API_KEY"]


# XXX? what is this for?
def create_request(config: dict):
    config_openai(config)
    headers = {"api-key": openai.api_key}

    deployment_name = config["OPENAI_API_DEPLOYMENT_NAME"]
    url_parts = {
        "base_url": openai.api_base,
        "deployment_name": deployment_name,
        "api_version": openai.api_version,
    }

    template = config["OPENAI_API_URL_ENDPOINT"]
    oTemplate = Template(template)
    url = oTemplate.substitute(**url_parts)
    printing.pprint(url)
    return requests.get(url, headers=headers)


def create_query(config: dict):
    params = {
        "engine": config["OPENAI_API_DEPLOYMENT_NAME"],
        "temperature": config.get("OPENAI_COMPLETION_TEMPERATURE"),
        "max_tokens": config.get("OPENAI_COMPLETION_MAX_TOKENS"),
        "top_p": config.get("OPENAI_COMPLETION_TOP_P"),
        "frequency_penalty": config.get("OPENAI_COMPLETION_PENALTY_FREQUENCY"),
        "presence_penalty": config.get("OPENAI_COMPLETION_PENALTY_PRESENCE"),
        "best_of": config.get("OPENAI_COMPLETION_BEST_OF"),
        "stop": config.get("OPENAI_COMPLETION_STOP"),
    }

    def createCompletion(prompt: str):
        kwargs = dict(params)
        kwargs["prompt"] = prompt
        printing.pprint(kwargs)

        config_openai(config)
        return openai.Completion.create(**kwargs)

    return createCompletion


def create_chat(config: dict, system_prompt: str = None):
    params = {
        "engine": config["OPENAI_API_DEPLOYMENT_NAME"],
        "temperature": config.get("OPENAI_COMPLETION_TEMPERATURE"),
        "max_tokens": config.get("OPENAI_COMPLETION_MAX_TOKENS"),
        "top_p": config.get("OPENAI_COMPLETION_TOP_P"),
        "frequency_penalty": config.get("OPENAI_COMPLETION_PENALTY_FREQUENCY"),
        "presence_penalty": config.get("OPENAI_COMPLETION_PENALTY_PRESENCE"),
        "stop": config.get("OPENAI_COMPLETION_STOP"),
    }

    system_message = {"role": "system", "content": system_prompt} if system_prompt else None
    system_messages = [system_message] if system_message else []

    def createChatCompletion(prompt, messages=[]):
        user_prompt = {"role": "user", "content": prompt}
        msgs = system_messages + messages + [user_prompt]
        kwargs = dict(params)
        kwargs["messages"] = msgs
        printing.pprint(kwargs)

        config_openai(config)
        return openai.ChatCompletion.create(**kwargs)

    return createChatCompletion


def create_embedding_query(config: dict):
    params = {"engine": config["OPENAI_API_DEPLOYMENT_NAME"]}

    def createEmbedding(text: str):
        config_openai(config)
        printing.pprint(text)
        printing.pprint(params)
        return get_embedding(text, **params)

    return createEmbedding


def get_first_choice(response: dict) -> dict:
    choices = response.choices
    first_choice = choices[0]
    return first_choice
