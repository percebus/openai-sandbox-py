from dataclasses import dataclass, field

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings


# SRC: https://github.com/microsoft/semantic-kernel/blob/main/python/README.md
@dataclass
class Summarizer:
    config: Configuration = field(default_factory=Configuration)

    kernel: Kernel = field(default_factory=Kernel)
    openai_client: AzureChatCompletion = field(init=False)
    functions: dict = field(init=False)  # dict[str, SKFunctionBase]

    @property
    def settings(self) -> Settings:
        return self.config.settings

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("gpt", self.openai_client)
        self.functions = {
            "summarize_in_5_words": Summarizer.create_semantic_function__summarize_in_5_words(self.kernel),
            "summarize_in_1_line_with_fewest_words": Summarizer.create_semantic_function__summarize_in_1_line_with_fewest_words(self.kernel),
        }

    @staticmethod
    def create_semantic_function__summarize_in_5_words(
        kernel: Kernel,
    ):  # -> SKFunctionBase:
        oSKFunction = kernel.create_semantic_function("{{$input}}\n\nGive me the TLDR in exactly 5 words.")
        return oSKFunction

    @staticmethod
    def create_semantic_function__summarize_in_1_line_with_fewest_words(
        kernel: Kernel,
    ):  # -> SKFunctionBase:
        oSKFunction = kernel.create_semantic_function("{{$input}}\n\nOne line TLDR with the fewest words.")
        return oSKFunction

    async def invoke(self, function_name: str, text: str):
        fn = self.functions[function_name]
        return fn(text)

    async def summarize_in_5_words(self, text: str):
        fn = self.functions["summarize_in_5_words"]
        return fn(text)

    async def summarize_in_1_line_with_fewest_words(self, text: str):
        fn = self.functions["summarize_in_1_line_with_fewest_words"]
        return fn(text)

    async def process_file(self, function_name: str, file_path: str):
        with open(file_path, encoding="utf-8") as oFile:
            contents = oFile.read()

        print(f"\n\n == {file_path} =================================")
        print(contents)

        #  Object of type "SKFunctionBase" is not callable
        summary = await self.invoke(function_name, contents)  # type: ignore
        print("\nTL;DR:")
        print(summary)
