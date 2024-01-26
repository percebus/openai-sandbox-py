from dataclasses import dataclass, field

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings


@dataclass
class FunPlugin:
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
        self.functions = FunPlugin.import_semantic_plugin(self.kernel)

    @staticmethod
    def import_semantic_plugin(kernel: Kernel, parent_directory: str = "data/semantic_kernel/plugins") -> dict:  # dict[str, SKFunctionBase]
        plugin_directory_name = "fun"
        functions: dict = kernel.import_semantic_plugin_from_directory(parent_directory, plugin_directory_name)
        return functions

    async def invoke(self, function_name: str, **kwargs):
        fn = self.functions[function_name]
        text = kwargs["input"]
        return fn(text)

    async def run(self, function_name: str, **kwargs):
        print(f'kwargs: "{kwargs}"')

        #  Object of type "SKFunctionBase" is not callable
        result = await self.invoke(function_name, **kwargs)  # type: ignore

        print("Result:")
        print(result)
