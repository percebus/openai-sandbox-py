#!/usr/bin/env python3

import pandas
import tiktoken
from dotenv import dotenv_values

from openai.embeddings_utils import cosine_similarity
from src.libs import env
from src.libs import api
from src.libs import printing
from src.libs import strings

ENV = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.az.openai.text-embedding-ada"),
}
config = env.parse(ENV)
printing.pprint(config)
query = api.create_embedding_query(config)


# Pick only columns we're interested in
def select_columns(oDataFrame, columns=["text", "summary", "title"]):
    return oDataFrame[columns]


# Remove things like whitespace
def clean_data(oDataFrame):
    oDataFrame["text"] = oDataFrame["text"].apply(strings.clean)
    return oDataFrame


def filter_rows(oDataFrame, encoding="cl100k_base", max_tokens=8192):
    tokenizer = tiktoken.get_encoding(encoding)
    oDataFrame["n_tokens"] = oDataFrame["text"].apply(
        lambda x: len(tokenizer.encode(x))
    )
    oDataFrame = oDataFrame[oDataFrame["n_tokens"] < max_tokens]
    return oDataFrame


def prepare_data(oDataFrame):
    printing.pprint(oDataFrame)
    subDataFrame = select_columns(oDataFrame.copy())
    cleanDataFrame = clean_data(subDataFrame.copy())
    filteredDataFrame = filter_rows(cleanDataFrame.copy())
    newDataFrame = filteredDataFrame  # .head(1) # Control how many rows
    printing.pprint(newDataFrame)
    return newDataFrame


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
    printing.pprint(newDataFrame)

    oDataFrame = pandas.read_csv(f"{folder}/samples/bill_sum_data.csv")
    newDataFrame = prepare_data(oDataFrame)

    newDataFrame["embedding"] = newDataFrame["text"].apply(lambda s: query(s))
    printing.pprint(newDataFrame)

    resultDataFrame = search(prompt, newDataFrame)
    printing.pprint(resultDataFrame)


if __name__ == "__main__":
    run()
