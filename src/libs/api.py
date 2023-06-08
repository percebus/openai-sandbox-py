import openai
import requests
from string import Template
from src.libs import printing


def config_openai(config):
    openai.api_type = config["OPENAI_API_TYPE"]
    openai.api_base = config["OPENAI_API_URL_BASE"]
    openai.api_version = config["OPENAI_API_VERSION"]
    openai.api_key = config["OPENAI_API_KEY"]


def create_query(config):
    params = {
        "engine": config["AZ_OPENAI_DEPLOYMENT_NAME"],
        "temperature": config.get("OPENAI_COMPLETION_TEMPERATURE"),
        "max_tokens": config.get("OPENAI_COMPLETION_MAX_TOKENS"),
        "top_p": config.get("OPENAI_COMPLETION_TOP_P"),
        "frequency_penalty": config.get("OPENAI_COMPLETION_PENALTY_FREQUENCY"),
        "presence_penalty": config.get("OPENAI_COMPLETION_PENALTY_PRESENCE"),
        "best_of": config.get("OPENAI_COMPLETION_BEST_OF"),
        "stop": config.get("OPENAI_COMPLETION_STOP"),
    }

    def query(prompt):
        kwargs = dict(params)
        kwargs["prompt"] = prompt
        printing.pprint(kwargs)

        config_openai(config)
        return openai.Completion.create(**kwargs)

    return query


def create_chat(config, system_prompt=None):
    params = {
        "engine": config["AZ_OPENAI_DEPLOYMENT_NAME"],
        "temperature": config.get("OPENAI_COMPLETION_TEMPERATURE"),
        "max_tokens": config.get("OPENAI_COMPLETION_MAX_TOKENS"),
        "top_p": config.get("OPENAI_COMPLETION_TOP_P"),
        "frequency_penalty": config.get("OPENAI_COMPLETION_PENALTY_FREQUENCY"),
        "presence_penalty": config.get("OPENAI_COMPLETION_PENALTY_PRESENCE"),
        "stop": config.get("OPENAI_COMPLETION_STOP"),
    }

    system_message = (
        {"role": "system", "content": system_prompt} if system_prompt else None
    )
    system_messages = [system_message] if system_message else []

    def ask(prompt, messages=[]):
        user_prompt = {"role": "user", "content": prompt}
        msgs = system_messages + messages + [user_prompt]
        kwargs = dict(params)
        kwargs["messages"] = msgs
        printing.pprint(kwargs)

        config_openai(config)
        return openai.ChatCompletion.create(**kwargs)

    return ask


def create_embedding_request(config):
    config_openai(config)
    headers = {
        'api-key': openai.api_key
    }

    deployment_name = config['AZ_OPENAI_DEPLOYMENT_NAME']
    url_parts = {
        'base_url': openai.api_base,
        'deployment_name': deployment_name,
        'api_version': openai.api_version
    }

    template = config['OPENAI_API_URL_ENDPOINT']
    oTemplate = Template(template)
    url = oTemplate.substitute(**url_parts)
    return requests.get(url, headers=headers)



def get_first_choice(response):
    choices = response.choices
    first_choice = choices[0]
    return first_choice
