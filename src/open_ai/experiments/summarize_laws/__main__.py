import asyncio

from dotenv import load_dotenv

from src.open_ai.semantickernel.clients.summarizer import SummarizerClient
from src.open_ai.semantickernel.functions.summarize_1_line import SummarizeIn1LineFunction
from src.open_ai.semantickernel.functions.summarize_five_words import SummarizeIn5WordsFunction


async def run():
    oSummarizerClient = SummarizerClient()
    await oSummarizerClient.process_file(SummarizeIn5WordsFunction, "data/facts/laws/asimov.txt")

    file_paths = [
        "data/facts/laws/thermodynamics.txt",
        "data/facts/laws/motion.txt",
        "data/facts/laws/universal_gravitation.txt",
    ]

    for file_path in file_paths:
        await oSummarizerClient.process_file(SummarizeIn1LineFunction, file_path)


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
