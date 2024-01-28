from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.plugin.semantic import SemanticPluginBase


@dataclass
class FunPlugin(SemanticPluginBase):
    plugin_directory_name: str = field(default="fun")
