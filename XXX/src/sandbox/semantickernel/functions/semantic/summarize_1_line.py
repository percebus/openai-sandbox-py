from dataclasses import dataclass, field

from open_ai.semantickernel.core.function.semantic import SemanticFunctionBase


@dataclass
class SummarizeIn1LineFunction(SemanticFunctionBase):
    prompt: str = field(default="{{$input}}\n\nOne line TLDR with the fewest words.")
