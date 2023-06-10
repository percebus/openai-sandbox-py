#!/usr/bin/env python3

import pandas
import tiktoken
from dotenv import dotenv_values

from src.libs import api, env, printing, strings

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.az.openai.text-embedding-ada"),  # ADA text-embedding
}
config = env.parse(ENV)
query = api.create_embedding_query(config)


# Pick only columns we're interested in
def select_columns(oDataFrame, columns):
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
    subDataFrame = select_columns(
        oDataFrame.copy(), columns=["text", "summary", "title"]
    )
    cleanDataFrame = clean_data(subDataFrame.copy())
    filteredDataFrame = filter_rows(cleanDataFrame.copy())
    newDataFrame = filteredDataFrame  # .head(1) # Control how many rows
    printing.pprint(newDataFrame)
    return newDataFrame


def run():
    folder = "./data/prompting/text/embedding/billing"

    oDataFrame = pandas.read_csv(f"{folder}/samples/bill_sum_data.csv")
    newDataFrame = prepare_data(oDataFrame)
    printing.pprint(newDataFrame)

    newDataFrame["embedding"] = newDataFrame["text"].apply(
        lambda s: query(s)  # pylint: disable=unnecessary-lambda
    )
    printing.pprint(newDataFrame)

    json_string = newDataFrame.to_json(orient="records")
    with open(f"{folder}/data/bills.json", "w", encoding="utf-8") as destFile:
        destFile.write(json_string)


if __name__ == "__main__":
    run()
