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
    with open("./data/prompts/classify/sentiment.txt") as oFile:
        prompt = "\n".join(oFile.readlines())

    print("Prompt:")
    oPrettyPrinter.pprint(prompt)

    response = query(prompt)
    oPrettyPrinter.pprint(response)
    # {
    #   "choices": [
    #     {
    #       "finish_reason": "stop",
    #       "index": 0,
    #       "logprobs": null,
    #       "text": "\nThe text displays a positive sentiment."
    #     }
    #   ],
    #   "created": 1685987746,
    #   "id": "cmpl-XXX",
    #   "model": "text-curie-001",
    #   "object": "text_completion",
    #   "usage": {
    #     "completion_tokens": 8,
    #     "prompt_tokens": 19,
    #     "total_tokens": 27
    #   }
    # }

    first_choice = response["choices"][0]
    result = first_choice["text"]  # The text displays a positive sentiment.
    print(result)


if __name__ == "__main__":
    run()
