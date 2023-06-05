#!/usr/bin/env python3

import common


def run():
    with open("./data/prompts/text/translate/fr-to-en/prompt.txt") as oFile:
        prompt = "\n".join(oFile.readlines())

    print("Prompt:")
    common.oPrettyPrinter.pprint(prompt)

    response = common.query(prompt)
    print(response)
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
