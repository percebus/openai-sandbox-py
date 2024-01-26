from dataclasses import dataclass, field

from src.open_ai.semantickernel.base.function import FunctionBase


@dataclass
class SummarizeIn1LineFunction(FunctionBase):
    prompt: str = field(default="{{$input}}\n\nOne line TLDR with the fewest words.")
