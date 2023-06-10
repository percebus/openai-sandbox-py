import redis


def createRedis(config: dict):
    return redis.Redis(
        host=config["REDIS_HOST"],
        port=config["REDIS_PORT"],
        password=config["REDIS_PASSWORD"],
    )
