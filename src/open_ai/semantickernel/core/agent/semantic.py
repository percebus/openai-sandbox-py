from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings
from src.open_ai.semantickernel.core.base import KernelBase


@dataclass
class SemanticAgentBase(KernelBase, ABC):
    config: Configuration = field(default_factory=Configuration)
    openai_client: AzureChatCompletion = field(init=False)

    def __post_init__(self):
        settings: Settings = self.settings
        self.openai_client = AzureChatCompletion(
            deployment_name=settings.openai_api_deployment_name,
            endpoint=settings.openai_api_base_url,
            api_key=settings.openai_api_key,
        )

        self.kernel.add_chat_service(settings.openai_api_type, self.openai_client)

    @property
    def settings(self) -> Settings:
        return self.config.settings
