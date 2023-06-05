#!/usr/bin/env python3

import os
import openai
import pprint

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_URL_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION", "2022-12-01")
openai.api_key = os.getenv("OPENAI_API_KEY")
AZ_OPENAI_DEPLOYMENT_NAME = os.getenv("AZ_OPENAI_DEPLOYMENT_NAME")

oPrettyPrinter = pprint.PrettyPrinter(indent=3)


def query(prompt):
    return openai.Completion.create(engine=AZ_OPENAI_DEPLOYMENT_NAME, prompt=prompt)


def run():
    with open("./data/prompts/translate/fr-to.en.txt") as oFile:
        prompt = "\n".join(oFile.readlines())

    print("Prompt:")
    oPrettyPrinter.pprint(prompt)

    response = query(engine=AZ_OPENAI_DEPLOYMENT_NAME, prompt=prompt)
    print(response)


if __name__ == "__main__":
    run()
