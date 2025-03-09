from dataclasses import dataclass, field

from sandbox.config.settings import Settings


@dataclass
class Configuration:
    settings: Settings = field(default_factory=Settings)  # type: ignore
