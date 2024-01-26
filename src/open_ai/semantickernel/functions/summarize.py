from semantic_kernel import Kernel


# SRC: https://github.com/microsoft/semantic-kernel/blob/main/python/README.md
def create_semantic_function__summarize_in_5_words(
    kernel: Kernel,
):  # -> SKFunctionBase:
    oSKFunction = kernel.create_semantic_function("{{$input}}\n\nGive me the TLDR in exactly 5 words.")

    return oSKFunction


def create_semantic_function__summarize_in_1_line_with_fewest_words(
    kernel: Kernel,
):  # -> SKFunctionBase:
    oSKFunction = kernel.create_semantic_function("{{$input}}\n\nOne line TLDR with the fewest words.")

    return oSKFunction
