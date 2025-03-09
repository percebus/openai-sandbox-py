from dataclasses import dataclass, field

from open_ai.semantickernel.core.plugin.semantic import SemanticPluginBase


@dataclass
class FunPlugin(SemanticPluginBase):
    plugin_directory_name: str = field(default="fun")
