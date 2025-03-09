from typing import Any

from redis import Redis


def createRedis(config: dict[str, Any]) -> Redis:
    return Redis(
        host=config["REDIS_HOST"],
        port=config["REDIS_PORT"],
        password=config["REDIS_PASSWORD"],
        encoding="utf-8",
        decode_responses=True,
    )
