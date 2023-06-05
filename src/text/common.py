import openai
import pprint
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.az.openai.text-curie"),
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.openai.params"),
}

openai.api_type = config["OPENAI_API_TYPE"]
openai.api_base = config["OPENAI_API_URL_BASE"]
openai.api_version = config["OPENAI_API_VERSION"]
openai.api_key = config["OPENAI_API_KEY"]
AZ_OPENAI_DEPLOYMENT_NAME = config["AZ_OPENAI_DEPLOYMENT_NAME"]
OPENAI_COMPLETION_TEMPERATURE = config.get("OPENAI_COMPLETION_TEMPERATURE")
OPENAI_COMPLETION_MAX_TOKENS = config.get("OPENAI_COMPLETION_MAX_TOKENS")
OPENAI_COMPLETION_TOP_P = config.get("OPENAI_COMPLETION_TOP_P")
OPENAI_COMPLETION_PENALTY_FREQUENCY = config.get("OPENAI_COMPLETION_PENALTY_FREQUENCY")
OPENAI_COMPLETION_PENALTY_PRESENCE = config.get("OPENAI_COMPLETION_PENALTY_PRESENCE")
OPENAI_COMPLETION_BEST_OF = config.get("OPENAI_COMPLETION_BEST_OF")
OPENAI_COMPLETION_STOP = config.get("OPENAI_COMPLETION_STOP")

temperature = int(OPENAI_COMPLETION_TEMPERATURE) if OPENAI_COMPLETION_TEMPERATURE is not None else None
max_tokens = int(OPENAI_COMPLETION_MAX_TOKENS) if OPENAI_COMPLETION_MAX_TOKENS is not None else None
top_p = int(OPENAI_COMPLETION_TOP_P) if OPENAI_COMPLETION_TOP_P is not None else None
frequency_penalty = int(OPENAI_COMPLETION_PENALTY_FREQUENCY) if OPENAI_COMPLETION_PENALTY_FREQUENCY is not None else None
presence_penalty = int(OPENAI_COMPLETION_PENALTY_PRESENCE) if OPENAI_COMPLETION_PENALTY_PRESENCE is not None else None
best_of = int(OPENAI_COMPLETION_BEST_OF) if OPENAI_COMPLETION_BEST_OF is not None else None
stop = OPENAI_COMPLETION_STOP.split(',') if OPENAI_COMPLETION_STOP is not None else None

oPrettyPrinter = pprint.PrettyPrinter(indent=3)

def query(prompt):

    kwargs = {
        'prompt': prompt,
        'engine': AZ_OPENAI_DEPLOYMENT_NAME,
        'temperature': temperature,
        'max_tokens': max_tokens,
        'top_p': top_p,
        'frequency_penalty': frequency_penalty,
        'presence_penalty': presence_penalty,
        'best_of': best_of,
        'stop': stop
    }
    oPrettyPrinter.pprint(kwargs)
    return openai.Completion.create(**kwargs)
