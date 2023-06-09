#!/usr/bin/env python3

import pandas
from dotenv import dotenv_values

from openai.embeddings_utils import cosine_similarity
from src.libs import env
from src.libs import api
from src.libs import printing

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.az.openai.text-embedding-ada"),  # ADA text-embedding
}
config = env.parse(ENV)
query = api.create_embedding_query(config)


def search(prompt, oDataFrame, top_n=3):
    question = query(prompt)
    oDataFrame["similarities"] = oDataFrame["embedding"].apply(
        lambda bill: cosine_similarity(bill, question)
    )

    return oDataFrame.sort_values("similarities", ascending=False).head(top_n)


def run():
    folder = "./data/prompting/text/embedding/billing"

    with open(f"{folder}/prompts/cable.txt") as oFile:
        prompt = oFile.read()

    oDataFrame = pandas.read_json(f"{folder}/data/bills.json")
    printing.pprint(oDataFrame)

    resultDataFrame = search(prompt, oDataFrame)
    printing.pprint(resultDataFrame)


if __name__ == "__main__":
    run()
