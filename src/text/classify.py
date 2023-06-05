#!/usr/bin/env python3

import common


def run():
    with open("./data/prompting/text/inferring/sentiment/Tweet/samples/trip.txt") as oFile:
        text = "\n".join(oFile.readlines())

    with open("./data/prompting/text/inferring/sentiment/Tweet/prompt.txt") as oFile:
        template = "\n".join(oFile.readlines())

    prompt = template.format(text=text)
    print("Prompt:")
    common.oPrettyPrinter.pprint(prompt)

    response = common.query(prompt)
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

    first_choice = response["choices"][0]
    result = first_choice["text"]  # "The text displays a positive sentiment."
    print(result)


if __name__ == "__main__":
    run()
