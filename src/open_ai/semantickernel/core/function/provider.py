import inspect
from dataclasses import dataclass, field

from semantic_kernel import Kernel

from src.open_ai.semantickernel.core.function.base import FunctionBase
from src.open_ai.semantickernel.functions import summarize_1_line, summarize_five_words

# TODO dynamically load all modules in functions folder
modules = [
    summarize_1_line,
    summarize_five_words,
]


@dataclass
class FunctionsProvier:
    kernel: Kernel = field(default_factory=Kernel)

    classes: dict[str, FunctionBase] = field(init=False)
    instances: dict[type[FunctionBase], FunctionBase] = field(init=False)

    def __post_init__(self):
        self.classes = {  # type
            name: item
            for module in modules
            for name, item in inspect.getmembers(module)
            if inspect.isclass(item) and issubclass(item, FunctionBase) and item != FunctionBase
        }

        self.instances = {Function: Function(kernel=self.kernel) for Function in self.classes.values()}
