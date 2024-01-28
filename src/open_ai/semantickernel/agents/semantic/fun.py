from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.semantickernel.core.agent.semantic import SemanticAgentBase
from src.open_ai.semantickernel.plugins.semantic.fun import FunPlugin


@dataclass
class FunAgent(SemanticAgentBase):
    plugin: FunPlugin = field(init=False)

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("gpt", self.openai_client)
        self.plugin = FunPlugin(kernel=self.kernel)

    async def invoke_async(self, function_name: str, **kwargs):
        fn = self.plugin.functions[function_name]
        text = kwargs["input"]
        return fn(text)

    async def run_async(self, function_name: str, **kwargs):
        print(f'kwargs: "{kwargs}"')

        #  Object of type "SKFunctionBase" is not callable
        result = await self.invoke_async(function_name, **kwargs)  # type: ignore

        print("Result:")
        print(result)
