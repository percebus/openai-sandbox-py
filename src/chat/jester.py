#!/usr/bin/env python3

import json
from dotenv import dotenv_values
from src.libs import env
from src.libs import api
from src.libs import printing


ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.az.openai.gpt-35-turbo"),  # ChatGPT
}
config = env.parse(ENV)
ask = api.create_chat(config)


def run():
    folder = "./data/prompting/chat/jester"

    # with open(f"{folder}/system/robot.txt") as oFile:
    # with open(f"{folder}/system/Alpha.txt") as oFile:
    # with open(f"{folder}/system/Shakespear.txt") as oFile:
    # with open(f"{folder}/system/Trump.txt") as oFile:
    with open(f"{folder}/system/Walken.txt") as oFile:
        system_prompt = oFile.read()

    ask = api.create_chat(config, system_prompt)

    with open(f"{folder}/messages/chicken.json") as oFile:
        json_string = oFile.read()

    messages = json.loads(json_string)
    printing.pprint(messages)

    # with open(f"{folder}/prompts/dislike.txt") as oFile:
    # with open(f"{folder}/prompts/ellipsis.txt") as oFile:
    with open(f"{folder}/prompts/dunno.txt") as oFile:
        prompt = oFile.read()

    response = ask(prompt, messages)
    print(response)

    choice = api.get_first_choice(response)
    answer = choice.message.content
    print(answer)  # To get to the other side, good sir!


if __name__ == "__main__":
    run()
