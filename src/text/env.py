transformers = {
    "OPENAI_COMPLETION_TEMPERATURE": float,
    "OPENAI_COMPLETION_MAX_TOKENS": int,
    "OPENAI_COMPLETION_TOP_P": float,
    "OPENAI_COMPLETION_PENALTY_FREQUENCY": float,
    "OPENAI_COMPLETION_PENALTY_PRESENCE": float,
    "OPENAI_COMPLETION_BEST_OF": int,
}


def parse(env):
    parsed = dict(env)
    for key, fn in transformers.items():
        value = env.get(key)
        if value is not None:
            parsed[key] = fn(value)

    return parsed