import redis


def createRedis(config: dict):
    return redis.Redis(
        host=config["REDIS_HOST"],
        port=config["REDIS_PORT"],
        password=config["REDIS_PASSWORD"],
        encoding="utf-8",
        decode_responses=True,
    )
