#!/usr/bin/env python3

import json
from dotenv import dotenv_values
from src.libs import env
from src.libs import api
from src.libs import printing


ENV = {
    **dotenv_values(".env.openai.api"),
    **dotenv_values(".env.az.openai.gpt-35-turbo"),
    **dotenv_values(".env.openai.params"),
}
config = env.parse(ENV)
ask = api.create_chat(config)


def run():
    folder = "./data/prompting/chat/Shakespearean"
    with open(f"{folder}/sessions/chicken.json") as oFile:
        json_string = oFile.read()

    session = json.loads(json_string)
    printing.pprint(session)

    # with open(f"{folder}/prompts/dislike.txt") as oFile:
    # with open(f"{folder}/prompts/ellipsis.txt") as oFile:
    with open(f"{folder}/prompts/dunno.txt") as oFile:
        prompt = oFile.read()

    response = ask(prompt, session)
    print(response)

    choice = api.get_first_choice(response)
    answer = choice.message.content
    print(answer)


if __name__ == "__main__":
    run()
