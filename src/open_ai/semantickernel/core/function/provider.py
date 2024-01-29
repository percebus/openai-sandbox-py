import inspect
from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.base import KernelBase
from src.open_ai.semantickernel.core.function.semantic import SemanticFunctionBase
from src.open_ai.semantickernel.functions.semantic import summarize_1_line, summarize_five_words

# TODO dynamically load all modules in
# from src.open_ai.semantickernel.functions.semantic
modules = [
    summarize_1_line,
    summarize_five_words,
]


@dataclass
class FunctionsProvier(KernelBase):
    classes: dict[str, SemanticFunctionBase] = field(init=False)
    instances: dict[type[SemanticFunctionBase], SemanticFunctionBase] = field(init=False)

    def __post_init__(self):
        self.classes = {  # type: ignore
            name: item
            for module in modules
            for name, item in inspect.getmembers(module)
            if inspect.isclass(item) and issubclass(item, SemanticFunctionBase) and item != SemanticFunctionBase
        }

        classes_names = self.classes.keys()
        print(f"loaded functions: {', '.join(classes_names)}")

        self.instances = {Function: Function(kernel=self.kernel) for Function in self.classes.values()}
