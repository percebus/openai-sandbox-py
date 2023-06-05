import os
import openai

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_URL_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION", "2022-12-01")
openai.api_key = os.getenv("OPENAI_API_KEY")
AZ_OPENAI_DEPLOYMENT_NAME = os.getenv("AZ_OPENAI_DEPLOYMENT_NAME")


def query(prompt):
    # endpoint = "{api_base_url}/openai/deployments/{deployment_name}/completions?api-version={api_version}"
    return openai.Completion.create(engine=AZ_OPENAI_DEPLOYMENT_NAME, prompt=prompt)
