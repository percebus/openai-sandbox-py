import math

from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.plugin_definition import sk_function, sk_function_context_parameter


class MathPlugin:
    @sk_function(
        name="Sqrt",
        description="Takes the square root of a number",
        input_description="The value to take the square root of",
    )
    def square_root(self, input_number: str) -> str:
        number = float(input_number)
        result = math.sqrt(number)
        return str(result)

    @sk_function(name="Add", description="Adds two numbers together")
    @sk_function_context_parameter(name="input", description="The first number to add")
    @sk_function_context_parameter(name="number2", description="The second number to add")
    def add(self, context: SKContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 + number2
        return str(result)

    @sk_function(name="Subtract", description="Subtract two numbers")
    @sk_function_context_parameter(name="input", description="The first number to subtract from")
    @sk_function_context_parameter(name="number2", description="The second number to subtract away")
    def subtract(self, context: SKContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 - number2
        return str(result)

    @sk_function(name="Multiply", description="Multiply two numbers. When increasing by a percentage, don't forget to add 1 to the percentage.")
    @sk_function_context_parameter(name="input", description="The first number to multiply")
    @sk_function_context_parameter(name="number2", description="The second number to multiply")
    def multiply(self, context: SKContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 * number2
        return str(result)

    @sk_function(name="Divide", description="Divide two numbers")
    @sk_function_context_parameter(name="input", description="The first number to divide from")
    @sk_function_context_parameter(name="number2", description="The second number to divide by")
    def divide(self, context: SKContext) -> str:
        number1 = float(context["input"])
        number2 = float(context["number2"])
        result: float = number1 / number2
        return str(result)
