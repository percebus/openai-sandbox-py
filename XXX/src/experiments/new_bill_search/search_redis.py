#!/usr/bin/env python3

import numpy
from dotenv import dotenv_values
from redis.commands.search.query import Query
from redis.exceptions import ResponseError

from src.open_ai.libs import api, cache, env

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.openai.text-embedding-ada"),  # ADA text-embedding
}
config = env.parse(ENV)
query = api.create_embedding_query(config)

oRedis = cache.createRedis(config)


def createVector(oEmbedding):
    return (
        numpy.array(oEmbedding)  # foreach
        .astype(numpy.float32)  # convert cooridnate
        .tobytes()
    )


def createQuery(top_n):
    return (
        Query(f"*=>[KNN {top_n} @embedding $vector AS vector_score]")
        .return_fields("title", "text", "vector_score")
        .sort_by("vector_score")
        .dialect(2)  # FIXME magic number
    )


def search(prompt, top_n=3):
    oEmbedding = query(prompt)
    queryVector = createVector(oEmbedding)
    redisQuery = createQuery(top_n)
    oResult = None
    try:
        oResult = oRedis.ft("bills").search(redisQuery, query_params={"vector": queryVector})
    except ResponseError as redisException:
        print("Error calling Redis search: ")
        print(redisException)

    return oResult


def run():
    folder = "./data/prompting/text/embedding/billing"

    with open(f"{folder}/prompts/cable.txt", encoding="utf-8") as oFile:
        prompt = oFile.read()

    oResult = search(prompt) or []
    print(f"Found {oResult.total} results:")
    for idx, bill in enumerate(oResult.docs):
        score = 1 - float(bill.vector_score)
        print(f"\t{idx}. {bill.title} (Score: {round(score, 3) })")


if __name__ == "__main__":
    run()
