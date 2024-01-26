import asyncio

from dotenv import load_dotenv

from src.open_ai.semantickernel.clients.fun import FunClient


async def run():
    oFunClient = FunClient()
    await oFunClient.run("joke", input="time travel to dinosaur age")


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
