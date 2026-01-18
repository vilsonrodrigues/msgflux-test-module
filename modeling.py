"""Simple greeting module for testing AutoModule."""

from msgflux.nn import Module


class GreetingModule(Module):
    """A simple module that generates greetings."""

    def __init__(self):
        super().__init__()

    def forward(self, name: str = "World") -> str:
        return f"Hello, {name}!"
