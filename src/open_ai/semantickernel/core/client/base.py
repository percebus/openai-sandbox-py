from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from src.open_ai.config.configuration import Configuration
from src.open_ai.config.settings import Settings


@dataclass
class ClientBase(ABC):
    config: Configuration = field(default_factory=Configuration)

    kernel: Kernel = field(default_factory=Kernel)
    openai_client: AzureChatCompletion = field(init=False)

    @property
    def settings(self) -> Settings:
        return self.config.settings
