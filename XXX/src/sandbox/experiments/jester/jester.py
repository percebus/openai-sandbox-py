#!/usr/bin/env python3

import json

from dotenv import dotenv_values

from open_ai.libs import api, env, printing

ENV = {
    **dotenv_values(".env"),  # Common config
    **dotenv_values(".env.openai.gpt-35-turbo"),  # ChatGPT
}
config = env.parse(ENV)
ask = api.create_chat(config)


def run():
    folder = "./assets/prompting/chat/jester"

    # with open(f"{folder}/system/robot.txt", encoding="utf-8") as oFile:
    # with open(f"{folder}/system/Alpha.txt", encoding="utf-8") as oFile:
    # with open(f"{folder}/system/Shakespear.txt", encoding="utf-8") as oFile:
    # with open(f"{folder}/system/Trump.txt", encoding="utf-8") as oFile:
    with open(f"{folder}/system/Walken.txt", encoding="utf-8") as oFile:
        system_prompt = oFile.read()

    ask = api.create_chat(config, system_prompt)  # pylint: disable=redefined-outer-name

    with open(f"{folder}/messages/chicken.json", encoding="utf-8") as oFile:
        json_string = oFile.read()

    messages = json.loads(json_string)
    printing.pprint(messages)

    # with open(f"{folder}/prompts/dislike.txt", encoding="utf-8") as oFile:
    # with open(f"{folder}/prompts/ellipsis.txt", encoding="utf-8") as oFile:
    with open(f"{folder}/prompts/dunno.txt", encoding="utf-8") as oFile:
        prompt = oFile.read()

    response = ask(prompt, messages)
    print(response)

    choice = api.get_first_choice(response)
    answer = choice.message.content
    print(answer)  # To get to the other side, good sir!


if __name__ == "__main__":
    run()
