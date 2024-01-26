from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.plugin.base import PluginBase


@dataclass
class FunPlugin(PluginBase):
    parent_directory: str = field(default="data/semantic_kernel/plugins")
    plugin_directory_name: str = field(default="fun")
