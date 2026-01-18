"""Simple greeting module for testing AutoModule."""

from msgflux.nn import Module


class GreetingModule(Module):
    """A simple module that generates greetings."""

    def __init__(self, language: str = "en"):
        super().__init__()
        self.language = language
        self._greetings = {
            "en": "Hello",
            "pt": "Olá",
            "es": "Hola",
            "fr": "Bonjour",
        }

    def forward(self, name: str = "World") -> str:
        greeting = self._greetings.get(self.language, "Hello")
        return f"{greeting}, {name}!"


# Pre-instantiated object for sharing_mode: instance
greeter = GreetingModule(language="pt")
