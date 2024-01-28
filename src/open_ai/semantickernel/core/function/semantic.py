from dataclasses import dataclass, field

from semantic_kernel import SKFunctionBase

from src.open_ai.semantickernel.core.base import KernelBase


@dataclass
class SemanticFunctionBase(KernelBase):
    prompt: str = field(init=False)
    function: SKFunctionBase = field(init=False)

    def __post_init__(self):
        self.function = self.kernel.create_semantic_function(self.prompt)

    def invoke(self, text: str):
        # FIXME  Object of type "SKFunctionBase" is not callable
        return self.function(text)  # type: ignore
