#!/usr/bin/env python3

from dotenv import dotenv_values

from src.open_ai.libs import api, env, printing

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.openai.text-curie"),
}
config = env.parse(ENV)
query = api.create_query(config)


def run():
    folder = "./data/prompting/text/translate/en"
    with open(f"{folder}/samples/hello.txt", encoding="utf-8") as oFile:
        text = oFile.read()

    with open(f"{folder}/to/fr/prompt.tpl.txt", encoding="utf-8") as oFile:
        template = oFile.read()

    prompt = template.format(text=text)
    print("Prompt:")
    printing.pprint(prompt)

    response = query(prompt)
    printing.pprint(response)
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

    choice = api.get_first_choice(response)
    print(choice.text)  # "Salut"


if __name__ == "__main__":
    run()
