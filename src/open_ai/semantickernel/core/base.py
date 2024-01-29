from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import Kernel


@dataclass
# TODO? RENAME?
#  - KernelContainerBase?
#  - KernelWrapperBase?
class KernelBase(ABC):
    kernel: Kernel = field(default_factory=Kernel)
