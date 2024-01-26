from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings
from src.open_ai.semantickernel.functions import summarize


def createKernel(openai_client: AzureChatCompletion) -> Kernel:
    oKernel = Kernel()
    oKernel.add_chat_service("gpt", openai_client)
    return oKernel


def process_file(file_path: str, semantic_function):
    with open(file_path, encoding="utf-8") as oFile:
        contents = oFile.read()

    print(f"\n\n == {file_path} =================================")
    print(contents)

    #  Object of type "SKFunctionBase" is not callable
    summary = semantic_function(contents)  # type: ignore
    print("\nTL;DR:")
    print(summary)


def run(settings: Settings):
    oAzureChatCompletion = AzureChatCompletion(
        deployment_name=settings.openai_api_deployment_name,
        endpoint=settings.openai_api_base_url,
        api_key=settings.openai_api_key,
    )

    oKernel: Kernel = createKernel(oAzureChatCompletion)
    summarize_in_5_words = summarize.create_semantic_function__summarize_in_5_words(oKernel)
    summarize_in_1_line_with_fewest_words = summarize.create_semantic_function__summarize_in_1_line_with_fewest_words(oKernel)

    process_file("data/facts/laws/asimov.txt", summarize_in_5_words)

    file_paths = [
        "data/facts/laws/thermodynamics.txt",
        "data/facts/laws/motion.txt",
        "data/facts/laws/universal_gravitation.txt",
    ]

    for file_path in file_paths:
        process_file(file_path, summarize_in_1_line_with_fewest_words)


def main():
    load_dotenv(".env.openai.gpt-35-turbo")
    oConfiguration = Configuration()
    oSettings: Settings = oConfiguration.settings
    run(oSettings)


if __name__ == "__main__":
    main()
