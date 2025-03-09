from dataclasses import dataclass, field

from open_ai.semantickernel.core.function.semantic import SemanticFunctionBase


@dataclass
class SummarizeIn5WordsFunction(SemanticFunctionBase):
    prompt: str = field(default="{{$input}}\n\nGive me the TLDR in exactly 5 words.")
