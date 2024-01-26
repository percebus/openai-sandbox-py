import asyncio

from dotenv import load_dotenv

from src.open_ai.experiments.summarize_laws.summarizer import Summarizer


async def run():
    oSummarizer = Summarizer()

    await oSummarizer.process_file("summarize_in_5_words", "data/facts/laws/asimov.txt")

    file_paths = [
        "data/facts/laws/thermodynamics.txt",
        "data/facts/laws/motion.txt",
        "data/facts/laws/universal_gravitation.txt",
    ]

    for file_path in file_paths:
        await oSummarizer.process_file("summarize_in_1_line_with_fewest_words", file_path)


async def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    await run()


if __name__ == "__main__":
    asyncio.run(main())
