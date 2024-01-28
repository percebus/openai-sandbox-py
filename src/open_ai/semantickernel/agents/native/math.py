from dataclasses import dataclass, field

from src.open_ai.semantickernel.core.agent.native import NativeAgentBase
from src.open_ai.semantickernel.plugins.native.math import MathPlugin


@dataclass
class MathAgent(NativeAgentBase):
    math_plugin: MathPlugin = field(default_factory=MathPlugin)

    def __post_init__(self):
        self.functions = self.kernel.import_plugin(self.math_plugin, plugin_name="math")

        function_names = self.functions.keys()
        print(f"loaded functions: {', '.join(function_names)}")

    async def invoke_async(self, function_name: str, **kwargs):
        fn = self.functions[function_name]
        return await self.kernel.run_async(fn, **kwargs)

    async def process_async(self, function_name: str, **kwargs):
        print(f"function: {function_name}")
        print(f'kwargs: "{kwargs}"')

        result = await self.invoke_async(function_name, **kwargs)
        print(f"Result: {result}")

        return result
