from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings
from src.open_ai.semantickernel.core.agent.semantic import SemanticAgentBase


@dataclass
class OpenAISemanticAgentBase(SemanticAgentBase):
    config: Configuration = field(default_factory=Configuration)
    openai_client: AzureChatCompletion = field(init=False)

    def __post_init__(self):
        self.openai_client = AzureChatCompletion(
            deployment_name=self.settings.openai_api_deployment_name,
            endpoint=self.settings.openai_api_base_url,
            api_key=self.settings.openai_api_key,
        )

        self.kernel.add_chat_service("openai", self.openai_client)

    @property
    def settings(self) -> Settings:
        return self.config.settings
