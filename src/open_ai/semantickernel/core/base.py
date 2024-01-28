from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import Kernel


@dataclass
class KernelBase(ABC):
    kernel: Kernel = field(default_factory=Kernel)
