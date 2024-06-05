from typing import Generator

from openai import OpenAI

from config import config


class ChatBot:
    def __init__(self, prompt: str, *, model: str = "gpt-3.5-turbo"):
        self._prompt = prompt
        self._model = model
        self._client = OpenAI(
            api_key=config.openai_config.api_key,
            base_url=config.openai_config.base_url,
        )

    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def model(self) -> str:
        return self._model

    def ask(self, stream: bool = False) -> str | Generator[str, None, None]:
        response = self._client.chat.completions.create(
            messages=[
                {
                    "role": 'system',
                    "content": self.prompt
                }],
            model=self.model,
            stream=stream
        )
        if not stream:
            return response.choices[0].message.content
        for chunk in response:
            chunk_message = chunk.choices[0].delta.content
            if chunk_message:
                yield chunk_message
