import openai
import pprint

oPrettyPrinter = pprint.PrettyPrinter(indent=3)
pprint = oPrettyPrinter.pprint


def config_openai(config):
    openai.api_type = config["OPENAI_API_TYPE"]
    openai.api_base = config["OPENAI_API_URL_BASE"]
    openai.api_version = config["OPENAI_API_VERSION"]
    openai.api_key = config["OPENAI_API_KEY"]


def create_query(config):
    config_openai(config)
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
        oPrettyPrinter.pprint(kwargs)
        return openai.Completion.create(**kwargs)

    return query


def get_first_result(response):
    first_choice = response["choices"][0]
    return first_choice["text"]
