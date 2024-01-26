import asyncio

from dotenv import load_dotenv

from src.open_ai.semantickernel.plugins.fun_plugin import FunPlugin


async def run():
    oFunPlugins = FunPlugin()
    await oFunPlugins.run("joke", input="time travel to dinosaur age")


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
