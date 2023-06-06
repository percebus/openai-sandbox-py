import openai
import pprint

oPrettyPrinter = pprint.PrettyPrinter(indent=3)

pprint = oPrettyPrinter.pprint

transformers = {
    'OPENAI_COMPLETION_TEMPERATURE': float,
    'OPENAI_COMPLETION_MAX_TOKENS': int,
    'OPENAI_COMPLETION_TOP_P': float,
    'OPENAI_COMPLETION_PENALTY_FREQUENCY': float,
    'OPENAI_COMPLETION_PENALTY_PRESENCE': float,
    'OPENAI_COMPLETION_BEST_OF': int
}

def create_query(config):
    def get_env_value(key):
        value = config.get(key)
        if value is None:
            return None

        fn = transformers.get(key)
        return fn(value) if fn else value

    openai.api_type = config["OPENAI_API_TYPE"]
    openai.api_base = config["OPENAI_API_URL_BASE"]
    openai.api_version = config["OPENAI_API_VERSION"]
    openai.api_key = config["OPENAI_API_KEY"]

    AZ_OPENAI_DEPLOYMENT_NAME = config["AZ_OPENAI_DEPLOYMENT_NAME"]
    OPENAI_COMPLETION_TEMPERATURE = get_env_value("OPENAI_COMPLETION_TEMPERATURE")
    OPENAI_COMPLETION_MAX_TOKENS = get_env_value("OPENAI_COMPLETION_MAX_TOKENS")
    OPENAI_COMPLETION_TOP_P = get_env_value("OPENAI_COMPLETION_TOP_P")
    OPENAI_COMPLETION_PENALTY_FREQUENCY = get_env_value(
        "OPENAI_COMPLETION_PENALTY_FREQUENCY"
    )
    OPENAI_COMPLETION_PENALTY_PRESENCE = get_env_value(
        "OPENAI_COMPLETION_PENALTY_PRESENCE"
    )
    OPENAI_COMPLETION_BEST_OF = get_env_value("OPENAI_COMPLETION_BEST_OF")
    OPENAI_COMPLETION_STOP = get_env_value("OPENAI_COMPLETION_STOP")

    def query(prompt):
        kwargs = {
            "prompt": prompt,
            "engine": AZ_OPENAI_DEPLOYMENT_NAME,
            "temperature": OPENAI_COMPLETION_TEMPERATURE,
            "max_tokens": OPENAI_COMPLETION_MAX_TOKENS,
            "top_p": OPENAI_COMPLETION_TOP_P,
            "frequency_penalty": OPENAI_COMPLETION_PENALTY_FREQUENCY,
            "presence_penalty": OPENAI_COMPLETION_PENALTY_PRESENCE,
            "best_of": OPENAI_COMPLETION_BEST_OF,
            "stop": OPENAI_COMPLETION_STOP,
        }
        oPrettyPrinter.pprint(kwargs)
        return openai.Completion.create(**kwargs)

    return query
