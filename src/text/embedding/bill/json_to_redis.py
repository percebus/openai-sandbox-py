import json

import numpy
from dotenv import dotenv_values

from src.libs import cache, env

ENV = {
    **dotenv_values(".env"),  # Common config
}
config = env.parse(ENV)


def run():
    folder = "./data/prompting/text/embedding/billing"

    with open(f"{folder}/data/bills.json", encoding="utf-8") as oFile:
        json_string = oFile.read()
    bills = json.loads(json_string)

    oRedis = cache.createRedis(config)
    redisPileline = oRedis.pipeline(transaction=False)
    for idx, bill in enumerate(bills):
        embedding = bill["embedding"]
        vector = numpy.array(embedding).astype(numpy.float32).tobytes()

        mapping = {
            "embedding": vector,
            "text": bill["text"],
        }

        print(f"Writing bill: ${idx}")
        print(mapping)
        oRedis.hset(name=f"bill:{idx}", mapping=mapping)

    redisPileline.execute()


if __name__ == "__main__":
    run()
