import math

from semantic_kernel.orchestration.kernel_context import KernelContext
from semantic_kernel.plugin_definition.kernel_function_context_parameter_decorator import kernel_function_context_parameter
from semantic_kernel.plugin_definition.kernel_function_decorator import kernel_function

from src.open_ai.semantickernel.core.plugin.native import NativePluginBase


class MathPlugin(NativePluginBase):
    @kernel_function(
        name="Sqrt",
        description="Takes the square root of a number",
        input_description="The value to take the square root of",
    )
    def square_root(self, input_number: str) -> str:
        number = float(input_number)
        result = math.sqrt(number)
        return str(result)

    @kernel_function(name="Add", description="Adds two numbers together")
    @kernel_function_context_parameter(name="input", description="The first number to add")
    @kernel_function_context_parameter(name="number2", description="The second number to add")
    def add(self, context: KernelContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 + number2
        return str(result)

    @kernel_function(name="Subtract", description="Subtract two numbers")
    @kernel_function_context_parameter(name="input", description="The first number to subtract from")
    @kernel_function_context_parameter(name="number2", description="The second number to subtract away")
    def subtract(self, context: KernelContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 - number2
        return str(result)

    @kernel_function(name="Multiply", description="Multiply two numbers. When increasing by a percentage, don't forget to add 1 to the percentage.")
    @kernel_function_context_parameter(name="input", description="The first number to multiply")
    @kernel_function_context_parameter(name="number2", description="The second number to multiply")
    def multiply(self, context: KernelContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 * number2
        return str(result)

    @kernel_function(name="Divide", description="Divide two numbers")
    @kernel_function_context_parameter(name="input", description="The first number to divide from")
    @kernel_function_context_parameter(name="number2", description="The second number to divide by")
    def divide(self, context: KernelContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 / number2
        return str(result)
