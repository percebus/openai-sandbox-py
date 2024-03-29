import asyncio

from dotenv import load_dotenv

from src.open_ai.semantickernel.agents.semantic.fun import FunAgent


async def run():
    oFunAgent = FunAgent()
    await oFunAgent.run_async("joke", input="time travel to dinosaur age")


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
