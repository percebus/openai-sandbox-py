from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from open_ai.libs.printing import pprint


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        case_sensitive=False,
        env_file=(  # Each file overrides the previous one
            ".env.inexistant",  # Inexistant file to test that it doesn't break
            ".env",  # lowest precedence
            ".env.openai.local",
            ".env.local",  # highest precedence
        ),
    )

    debug: Optional[bool] = Field(default=False)

    # TODO? Move these to a SubModel
    openai_api_type: str = Field(strict=True, default="azure")
    openai_api_model: str = Field(strict=True)
    openai_api_deployment_name: str = Field(strict=True)
    openai_api_base_url: str = Field(strict=True)
    openai_api_key: str = Field(strict=True)
    openai_api_version: str = Field(strict=True)

    def safe_model_dump(self):
        # TODO if not self.debug:
        # Filter out sensitive fields
        return self.model_dump() if self.debug else None


def main():
    settings = Settings()  # type: ignore
    pprint(settings.safe_model_dump())


if __name__ == "__main__":
    main()
