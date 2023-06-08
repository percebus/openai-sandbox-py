#!/usr/bin/env python3

from src.libs import env
from src.libs import api
from src.libs import printing
from dotenv import dotenv_values
import pandas

ENV = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.az.openai.text-embedding-ada"),
}
config = env.parse(ENV)
printing.pprint(config)
request = api.create_embedding_request(config)


def run():
    folder = "./data/embedding/billing"
    csv = pandas.read_csv(f"{folder}/bull_sum_data.csv")
    printing.pprint = csv


if __name__ == "__main__":
    run()
