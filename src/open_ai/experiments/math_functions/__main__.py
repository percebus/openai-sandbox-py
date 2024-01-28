from src.open_ai.semantickernel.agents.native.math import MathAgent


async def run():
    oMathAgent = MathAgent()

    result = await oMathAgent.process("Sqrt", input_str="12")

    # FIXME: pass 'number2'
    result = await oMathAgent.process("Add", input_str="1", input_vars={"number2": "2"})
    result = await oMathAgent.process("Subtract", input_str="3", input_vars={"number2": "2"})
    result = await oMathAgent.process("Multiply", input_str="2", input_vars={"number2": "3"})
    result = await oMathAgent.process("Divide", input_str="6", input_vars={"number2": "3"})

    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
