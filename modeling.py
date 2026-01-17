"""Simple greeting module for testing AutoModule."""

from msgflux.nn import Module


class GreetingModule(Module):
    """A simple module that generates greetings.

    This module demonstrates the basic structure needed for sharing
    modules via msgflux AutoModule.

    Example:
        >>> greeter = GreetingModule(language="pt")
        >>> greeter("msgflux")
        'Olá, msgflux!'
    """

    def __init__(self, language: str = "en"):
        """Initialize the greeting module.

        Args:
            language: Language for greeting ("en", "pt", "es", "fr").
        """
        super().__init__()
        self.language = language
        self._greetings = {
            "en": "Hello",
            "pt": "Olá",
            "es": "Hola",
            "fr": "Bonjour",
        }

    def forward(self, name: str = "World") -> str:
        """Generate a greeting message.

        Args:
            name: Name to greet.

        Returns:
            Greeting string.
        """
        greeting = self._greetings.get(self.language, "Hello")
        return f"{greeting}, {name}!"
