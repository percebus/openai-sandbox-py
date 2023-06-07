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
    folder = "./data/prompting/chat/friendly"

    # with open(f"{folder}/messages/empty.json") as oFile:
    with open(f"{folder}/messages/Isa.json") as oFile:
        json_string = oFile.read()

    messages = json.loads(json_string)
    printing.pprint(messages)

    with open(f"{folder}/system/friendly.txt") as oFile:
        system_prompt = oFile.read()

    instruction = {"role": "system", "content": system_prompt}
    session = [instruction] + messages

    # with open(f"{folder}/prompts/Isa.txt") as oFile:
    with open(f"{folder}/prompts/whoAmI.txt") as oFile:
        prompt = oFile.read()

    response = ask(prompt, session)
    print(response)

    choice = api.get_first_choice(response)
    answer = choice.message.content
    print(answer)  # To get to the other side, good sir!


if __name__ == "__main__":
    run()
