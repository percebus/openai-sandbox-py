transformers = {
    "AZ_OPENAI_MODEL_DIM": int,
    "OPENAI_COMPLETION_TEMPERATURE": float,
    "OPENAI_COMPLETION_MAX_TOKENS": int,
    "OPENAI_COMPLETION_TOP_P": float,
    "OPENAI_COMPLETION_PENALTY_FREQUENCY": float,
    "OPENAI_COMPLETION_PENALTY_PRESENCE": float,
    "OPENAI_COMPLETION_BEST_OF": int,
    "REDIS_PORT": int,
}


def parse(env: dict) -> dict:
    parsed = dict(env)
    for key, fn in transformers.items():
        value = env.get(key)
        if value is not None:
            parsed[key] = fn(value)

    return parsed
