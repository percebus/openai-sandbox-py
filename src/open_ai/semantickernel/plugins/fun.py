from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.plugin.base import PluginBase


@dataclass
class FunPlugin(PluginBase):
    plugin_directory_name: str = field(default="fun")
