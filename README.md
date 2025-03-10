# My OpenAI SandBox

[`TODO`s](./TODO.md) | [`LICENSE`](./LICENSE.md)

[![[C]ontinuous [I]ntegration](https://github.com/percebus/openai-sandbox-py/actions/workflows/always.yml/badge.svg)](https://github.com/percebus/openai-sandbox-py/actions/workflows/always.yml)

## Responsible AI

Usage of Azure OpenAI should follow the six Microsoft [AI principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai):

- Fairness: AI systems shouldn't make decisions that discriminate against or support bias of a group or individual.
- Reliability and Safety: AI systems should respond safely to new situations and potential manipulation.
- Privacy and Security: AI systems should be secure and respect data privacy.
- Inclusiveness: AI systems should empower everyone and engage people.
- Accountability: People must be accountable for how AI systems operate.
- Transparency: AI systems should have explanations so users can understand how they're built and used.

## Tokens

One token is roughly four characters for typical English text.

## Models

In the [Azure OpenAI Studio](https://oai.azure.com/portal), you can build AI models and deploy them for public consumption in software applications. Azure OpenAI's capabilities are made possible by specific generative AI models. Different models are optimized for different tasks; some models excel at summarization and providing general unstructured responses, and others are built to generate code or unique images from text input.

These Azure OpenAI models fall into a few main families:

- GPT-4
- GPT-3
- Codex
- [Embeddings](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/understand-embeddings)
- DALL-E

Azure OpenAI's AI models can all be trained and customized with [fine-tuning](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/fine-tuning?pivots=programming-language-studio%3Fazure-portal%3Dtrue). We won't go into custom models here, but you can learn more on the fine-tuning your model Azure documentation.

### GPT

Understanding GPT models for natural language generation
Generative pre-trained transformer (GPT) models are excellent at both understanding and creating natural language. If you've seen recent news around AI answering questions or writing a paragraph based on a prompt, it likely could have been generated by a GPT model. GPT models often have the version appended to the end, such as GPT-3 or GPT-4. Azure OpenAI offers preview access to ChatGPT powered by gpt-35-turbo and to GPT-4. You can apply for access to GPT-4 here.

What does a response from a GPT model look like?
A key aspect of OpenAI's generative AI is that it takes an input, or prompt, to return a natural language, visual, or code response. GPT tries to infer, or guess, the context of the user's question based on the prompt.

#### Prompts

GPT models are great at completing several natural language tasks, some of which include:

| Task                        | Prompt                                   |
| --------------------------- | ---------------------------------------- |
| Summarizing text            | "Summarize this text into a short blurb" |
| Classifying text            | "What genre of book is this?"            |
| Generating names or phrases | "Write a tagline for my flower company"  |
| Translation                 | "Translate 'How are you' to French"      |
| Answering questions         | "What does Azure OpenAI do?"             |
| Suggesting content          | "Give me the five best weddings songs"   |

Prompts can be grouped into types of requests based on task.

Learn more about [prompt engineering](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/prompt-engineering?portal=true).

| Task type                                          | Prompt example                          | Completion example                                                                                                            |
| -------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Classifying content                                | Tweet: I enjoyed the trip. Sentiment:   | Positive                                                                                                                      |
| Generating new content                             | List ways of traveling                  | 1. Bike 2. Car ...                                                                                                            |
| Holding a conversation                             | A friendly AI assistant                 | [See examples](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/completions#conversation?portal=true) |
| Transformation (translation and symbol conversion) | English: Hello, French:                 | bonjour                                                                                                                       |
| Summarizing content                                | Provide a summary of the content {text} | The content shares methods of machine learning.                                                                               |
| Picking up where you left off                      | One way to grow tomatoes                | is to plant seeds.                                                                                                            |
| Giving factual responses                           | How many moons does Earth have?         | One                                                                                                                           |

#### Prompting Principles

##### Write clear and specific instructions

- Use delimeters

  - `###`
  - `"""`
  - 3x `
  - `---`
  - `<` `>`
  - `<tag>`XML`</tag>`

- Ask for structured ouptut:

  - HTML
  - JSON

- Check

  - Wether conditions are satisfied.
  - Assumptions required to do the ask.

- Few-shot prompting.

##### Give the model time to "think"

- Specify the steps required to complete a task.
- Instruct the model to work out its own solution before rushing to a conclusion.
- Reduce hallucinations.
  - First find relevant information.
  - Answer the question based on relevant information.

## Repositories

- [`openai/openai-cookbook`](https://github.com/openai/openai-cookbook)
- [`MicrosoftLearning/mslearn-openai`](https://github.com/MicrosoftLearning/mslearn-openai)
- [`Azure-samples/Azure-OpenAI-Docs-Samples`](https://github.com/Azure-samples/Azure-OpenAI-Docs-Samples)

## Tutorials

- [Storing and querying for embeddings with Redis](https://blog.baeke.info/2023/03/21/storing-and-querying-for-embeddings-with-redis/)

### MS Learn

- [Introduction to Azure OpenAI Service](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/)
- [Get started with Azure OpenAI Service](https://microsoftlearning.github.io/mslearn-openai/Instructions/Labs/01-get-started-azure-openai.html)
- [Integrate Azure OpenAI into your app](https://microsoftlearning.github.io/mslearn-openai/Instructions/Labs/02-natural-language-azure-openai.html)
- [Utilize prompt engineering in your app](https://microsoftlearning.github.io/mslearn-openai/Instructions/Labs/03-prompt-engineering.html)
- [Explore Azure OpenAI Service embeddings and document search](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/tutorials/embeddings?tabs=command-line)

### DeepLearning.AI

- [ChatGTP Prompt Engineering for Developers](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction)
- [Building Systems with the ChatGPT API](https://learn.deeplearning.ai/chatgpt-building-system/)

## Resources

### AI

- [Deep learning vs. machine learning in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-deep-learning-vs-machine-learning?view=azureml-api-2)

### OpenAI

- [OpenAI Examples](https://platform.openai.com/examples)
- [OpenAI Python Library](https://pypi.org/project/openai/)
- [Text Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- [Understanding embeddings in Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/understand-embeddings)
- [New and improved embedding model](https://openai.com/blog/new-and-improved-embedding-model)
- [What are tokens and how to count them?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

### [L]arge [L]anguage [M]odels

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)

### LangChain

- [Prompt Templates](https://python.langchain.com/en/latest/modules/prompts/prompt_templates.html)
- [Output Parsers](https://python.langchain.com/en/latest/modules/prompts/output_parsers.html)
- [Chains](https://python.langchain.com/en/latest/modules/chains.html)
- [Tools](https://python.langchain.com/en/latest/modules/agents/tools.html)
- [Agents](https://python.langchain.com/en/latest/modules/agents.html)
