from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.function.base import FunctionBase


@dataclass
class SummarizeIn5WordsFunction(FunctionBase):
    prompt: str = field(default="{{$input}}\n\nGive me the TLDR in exactly 5 words.")
