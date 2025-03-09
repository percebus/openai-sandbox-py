from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import KernelFunctionBase

from open_ai.semantickernel.core.base import KernelBase


@dataclass
class SemanticFunctionBase(KernelBase, ABC):
    prompt: str = field(init=False)
    function: KernelFunctionBase = field(init=False)

    def __post_init__(self):
        self.function = self.kernel.create_semantic_function(self.prompt)

    def invoke(self, text: str):
        # FIXME  Object of type "KernelFunctionBase" is not callable
        return self.function(text)  # type: ignore
