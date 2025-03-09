from dataclasses import dataclass, field

from open_ai.semantickernel.core.agent.native import NativeAgentBase
from open_ai.semantickernel.plugins.native.math import MathPlugin


@dataclass
class MathAgent(NativeAgentBase):
    math_plugin: MathPlugin = field(default_factory=MathPlugin)

    def __post_init__(self):
        self.functions = self.kernel.import_plugin(self.math_plugin, plugin_name="math")

        function_names = self.functions.keys()
        print(f"loaded functions: {', '.join(function_names)}")

    def invoke(self, function_name: str, **kwargs):
        fn = self.functions[function_name]
        return self.kernel.run(fn, **kwargs)

    def process(self, function_name: str, **kwargs):
        print(f"function: {function_name}")
        print(f'kwargs: "{kwargs}"')

        result = self.invoke(function_name, **kwargs)
        print(f"Result: {result}")

        return result
