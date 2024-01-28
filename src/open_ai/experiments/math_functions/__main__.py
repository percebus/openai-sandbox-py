from src.open_ai.semantickernel.agents.native.math import MathAgent


async def run():
    oMathAgent = MathAgent()

    result = await oMathAgent.process_async("Sqrt", input_str="12")

    # FIXME: pass 'number2'
    result = await oMathAgent.process_async("Add", input_str="1", input_vars={"number2": "2"})
    result = await oMathAgent.process_async("Subtract", input_str="3", input_vars={"number2": "2"})
    result = await oMathAgent.process_async("Multiply", input_str="2", input_vars={"number2": "3"})
    result = await oMathAgent.process_async("Divide", input_str="6", input_vars={"number2": "3"})

    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
