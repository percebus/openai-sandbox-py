#!/usr/bin/env python3

from src.lib import env
from src.lib import api
from src.lib import printing
from dotenv import dotenv_values

ENV = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.openai.params"),
    **dotenv_values(".env.az.openai.text-curie"),
}
config = env.parse(ENV)
query = api.create_query(config)


def run():
    folder = "./data/prompting/text/inferring/sentiment/Tweet"
    with open(f"{folder}/samples/trip.txt") as oFile:
        text = oFile.read()

    with open(f"{folder}/prompt.tpl.txt") as oFile:
        template = oFile.read()

    prompt = template.format(text=text)
    print("Prompt:")
    printing.pprint(prompt)

    response = query(prompt)
    print(response)
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

    result = api.get_first_result(response)
    print(result)  # "The text displays a positive sentiment."


if __name__ == "__main__":
    run()
