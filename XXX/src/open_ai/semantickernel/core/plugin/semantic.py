from abc import ABC
from dataclasses import dataclass, field

from open_ai.semantickernel.core.base import KernelBase


@dataclass
class SemanticPluginBase(KernelBase, ABC):
    parent_directory: str = field(default="assets/semantic_kernel/plugins")
    plugin_directory_name: str = field(init=False)

    functions: dict = field(init=False)  # dict[str, KernelFunctionBase]

    def __post_init__(self):
        self.functions = self.kernel.import_semantic_plugin_from_directory(self.parent_directory, self.plugin_directory_name)
