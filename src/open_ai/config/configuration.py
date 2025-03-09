from dataclasses import dataclass, field

from open_ai.config.settings import Settings


@dataclass
class Configuration:
    settings: Settings = field(default_factory=Settings)  # type: ignore
