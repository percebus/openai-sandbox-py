from abc import ABC
from dataclasses import dataclass, field

from open_ai.semantickernel.core.base import KernelBase


@dataclass
class NativeAgentBase(KernelBase, ABC):
    functions: dict = field(init=False)  # dict[str, KernelFunctionBase]
