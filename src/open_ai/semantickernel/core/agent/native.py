from abc import ABC
from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.base import KernelBase


@dataclass
class NativeAgentBase(KernelBase, ABC):
    functions: dict = field(init=False)  # dict[str, KernelFunctionBase]
