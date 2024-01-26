from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.semantickernel.core.client.base import ClientBase
from src.open_ai.semantickernel.core.function.base import FunctionBase
from src.open_ai.semantickernel.core.function.provider import FunctionsProvier


# SRC: https://github.com/microsoft/semantic-kernel/blob/main/python/README.md
@dataclass
class FunctionsClient(ClientBase):
    functions_provider: FunctionsProvier = field(init=False)

    @property
    def functions(self) -> dict[type[FunctionBase], FunctionBase]:
        return self.functions_provider.instances

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("gpt", self.openai_client)

        self.functions_provider = FunctionsProvier(kernel=self.kernel)

    async def process_file(self, Function: type[FunctionBase], file_path: str):
        with open(file_path, encoding="utf-8") as oFile:
            contents = oFile.read()

        print(f"\n\n == {file_path} =================================")
        print(contents)

        #  Object of type "SKFunctionBase" is not callable
        oFunction = self.functions[Function]
        summary = oFunction.semantic_function(contents)  # type: ignore
        print("\nTL;DR:")
        print(summary)
