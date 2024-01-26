from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import Kernel


@dataclass
class PluginBase(ABC):
    kernel: Kernel = field(default_factory=Kernel)
    parent_directory: str = field(default="data/semantic_kernel/plugins")
    plugin_directory_name: str = field(init=False)
    functions: dict = field(init=False)  # dict[str, SKFunctionBase]

    def __post_init__(self):
        self.functions = self.kernel.import_semantic_plugin_from_directory(self.parent_directory, self.plugin_directory_name)
