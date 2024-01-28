from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.base import KernelBase


@dataclass
class NativeAgentBase(KernelBase):
    functions: dict = field(init=False)  # dict[str, SKFunctionBase]
