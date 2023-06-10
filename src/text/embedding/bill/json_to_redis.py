import json

import numpy
from dotenv import dotenv_values
from redis.commands.search.field import TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

from src.libs import cache, env, vectors

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.az.openai.text-embedding-ada"),  # ADA text-embedding
}
config = env.parse(ENV)

PREFIX = "bill"
oRedis = cache.createRedis(config)


def try_create_index(fields, definition):
    oRedis.ft("bills").create_index(fields=fields, definition=definition)
    # try:
    #     # Create the index
    # except Exception as e:
    #     print("Index already exists")


def load_data(bills):
    for idx, bill in enumerate(bills):
        embedding = bill["embedding"]
        _vector = numpy.array(embedding).astype(numpy.float32).tobytes()

        mapping = {
            "embedding": _vector,
            "text": bill["text"],
        }

        print(f"Writing bill: ${idx}")
        print(mapping)
        key = f"{PREFIX}:{idx}"
        oRedis.hset(name=key, mapping=mapping)


def run():
    folder = "./data/prompting/text/embedding/billing"

    with open(f"{folder}/data/bills.json", encoding="utf-8") as oFile:
        json_string = oFile.read()
    bills = json.loads(json_string)

    load_data(bills)
    redisPileline = oRedis.pipeline(transaction=False)
    redisPileline.execute()

    dim = (config["AZ_OPENAI_MODEL_DIM"],)  # 1536 for ada-002
    fields = [
        VectorField(
            "embedding",
            vectors.Algorithms.HNSW,
            {
                "TYPE": "FLOAT",
                "DIM": dim,
                "DISTANCE": vectors.DistanceMetrics.CoSine,
            },
        ),
        TextField("text"),
    ]
    prefixes = [f"{PREFIX}:"]
    oIndexDefinition = IndexDefinition(prefix=prefixes, index_type=IndexType.HASH)
    try_create_index(fields, oIndexDefinition)


if __name__ == "__main__":
    run()
