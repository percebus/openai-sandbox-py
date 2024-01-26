from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.semantickernel.base.app import AppBase
from src.open_ai.semantickernel.base.function import FunctionBase
from src.open_ai.semantickernel.functions.summarize_1_line import SummarizeIn1LineFunction
from src.open_ai.semantickernel.functions.summarize_five_words import SummarizeIn5WordsFunction


# SRC: https://github.com/microsoft/semantic-kernel/blob/main/python/README.md
@dataclass
class Summarizer(AppBase):
    functions: dict[str, FunctionBase] = field(init=False)

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("gpt", self.openai_client)

        self.functions = {}
        self.functions["SummarizeIn5WordsFunction"] = SummarizeIn5WordsFunction(kernel=self.kernel)
        self.functions["SummarizeIn1LineFunction"] = SummarizeIn1LineFunction(kernel=self.kernel)

    async def process_file(self, function_name: str, file_path: str):
        with open(file_path, encoding="utf-8") as oFile:
            contents = oFile.read()

        print(f"\n\n == {file_path} =================================")
        print(contents)

        #  Object of type "SKFunctionBase" is not callable
        oFunction = self.functions[function_name]
        summary = oFunction.semantic_function(contents)  # type: ignore
        print("\nTL;DR:")
        print(summary)
