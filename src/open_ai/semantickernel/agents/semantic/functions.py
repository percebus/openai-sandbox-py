from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.semantickernel.core.agent.semantic import SemanticAgentBase
from src.open_ai.semantickernel.core.function.provider import FunctionsProvier
from src.open_ai.semantickernel.core.function.semantic import SemanticFunctionBase


# SRC: https://github.com/microsoft/semantic-kernel/blob/main/python/README.md
@dataclass
class SemanticFunctionsAgent(SemanticAgentBase):
    functions_provider: FunctionsProvier = field(init=False)

    @property
    def functions(self) -> dict[type[SemanticFunctionBase], SemanticFunctionBase]:
        return self.functions_provider.instances

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("gpt", self.openai_client)

        self.functions_provider = FunctionsProvier(kernel=self.kernel)

    async def process_file_async(self, Function: type[SemanticFunctionBase], file_path: str):
        with open(file_path, encoding="utf-8") as oFile:
            contents = oFile.read()

        print(f"\n\n == {file_path} =================================")
        print(contents)

        #  Object of type "KernelFunctionBase" is not callable
        oFunction = self.functions[Function]
        summary = oFunction.function(contents)  # type: ignore
        print("\nTL;DR:")
        print(summary)

        return summary
