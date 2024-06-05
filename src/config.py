from dataclasses import dataclass

from environs import Env


@dataclass
class ModelConfig:
    available_models: list

    @staticmethod
    def from_env(env: Env):
        return ModelConfig(
            available_models=env.list("AVAILABLE_MODELS"),
        )


@dataclass
class OpenAIConfig:
    api_key: str
    base_url: str

    @staticmethod
    def from_env(env: Env):
        return OpenAIConfig(
            api_key=env.str("OPENAI_API_KEY"),
            base_url=env.str("OPENAI_BASE_URL"),
        )


@dataclass
class Config:
    model_config: ModelConfig
    openai_config: OpenAIConfig


def load_config(path: str = ".env") -> Config:
    env = Env()
    env.read_env(path=path)
    return Config(
        model_config=ModelConfig.from_env(env=env),
        openai_config=OpenAIConfig.from_env(env=env)
    )


config = load_config()
