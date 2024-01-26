from abc import ABC
from dataclasses import dataclass, field

from semantic_kernel import Kernel, SKFunctionBase


@dataclass
class FunctionBase(ABC):
    prompt: str = field(init=False)
    kernel: Kernel = field(default_factory=Kernel)
    semantic_function: SKFunctionBase = field(init=False)

    def __post_init__(self):
        self.semantic_function = self.kernel.create_semantic_function(self.prompt)

    def invoke(self, text: str):
        # FIXME  Object of type "SKFunctionBase" is not callable
        return self.semantic_function(text)  # type: ignore
