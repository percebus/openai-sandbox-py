#!/usr/bin/env python3

import openai
import os

OPENAI_SECRET = os.getenv("OPENAI_API_KEY")


def run():
    print("Hello, World!")


if __name__ == "__main__":
    run()
