import asyncio

from dotenv import load_dotenv

from src.open_ai.semantickernel.agents.semantic.functions import SemanticFunctionsAgent
from src.open_ai.semantickernel.functions.semantic.summarize_1_line import SummarizeIn1LineFunction
from src.open_ai.semantickernel.functions.semantic.summarize_five_words import SummarizeIn5WordsFunction


async def run():
    oSemanticFunctionsAgent = SemanticFunctionsAgent()
    await oSemanticFunctionsAgent.process_file_async(SummarizeIn5WordsFunction, "assets/facts/laws/asimov.txt")

    file_paths = [
        "assets/facts/laws/thermodynamics.txt",
        "assets/facts/laws/motion.txt",
        "assets/facts/laws/universal_gravitation.txt",
    ]

    for file_path in file_paths:
        await oSemanticFunctionsAgent.process_file_async(SummarizeIn1LineFunction, file_path)


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
