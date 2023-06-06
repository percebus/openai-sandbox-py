#!/usr/bin/env python3

import common
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.openai.params"),
    **dotenv_values(".env.az.openai.text-curie"),
}

query = common.create_query(config)


def run():
    folder = "./data/prompting/text/translate/en"
    with open(f"{folder}/samples/hello.txt") as oFile:
        text = "\n".join(oFile.readlines())

    with open(f"{folder}/to/fr/prompt.txt") as oFile:
        template = "\n".join(oFile.readlines())

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
    #         "text": "\nBonjour"
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

    first_choice = response["choices"][0]
    result = first_choice["text"]  # "Bonjour"
    print(result)


if __name__ == "__main__":
    run()
