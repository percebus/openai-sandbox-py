#!/usr/bin/env python3

import env
import common
from dotenv import dotenv_values

ENV = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.openai.params"),
    **dotenv_values(".env.az.openai.text-curie"),
}
config = env.parse(ENV)
query = common.create_query(config)


def run():
    folder = "./data/prompting/text/translate/en"
    with open(f"{folder}/samples/hello.txt") as oFile:
        text = oFile.read()

    with open(f"{folder}/to/fr/prompt.txt") as oFile:
        template = oFile.read()

    prompt = template.format(text=text)
    print("Prompt:")
    common.pprint(prompt)

    response = query(prompt)
    common.pprint(response)
    # {
    #     "choices": [
    #     {
    #         "finish_reason": "stop",
    #         "index": 0,
    #         "logprobs": null,
    #         "text": "\n\nSalut"
    #     }
    #     ],
    #     "created": 1685993770,
    #     "id": "cmpl-XXX",
    #     "model": "text-curie-001",
    #     "object": "text_completion",
    #     "usage": {
    #     "completion_tokens": 4,
    #     "prompt_tokens": 12,
    #     "total_tokens": 16
    #     }
    # }

    result = common.get_first_result(response)
    print(result)  # "Salut"


if __name__ == "__main__":
    run()
