"""
Custom exceptions used throughout the Trinetra AI backend.

Having custom exceptions allows every provider to raise meaningful,
consistent errors instead of generic Exception objects.
"""


class TrinetraException(Exception):
    """Base exception for the Trinetra AI project."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ProviderError(TrinetraException):
    """Raised when a provider encounters an error."""


class InvalidAPIKeyError(ProviderError):
    """Raised when an API key is invalid or missing."""


class RateLimitError(ProviderError):
    """Raised when an API rate limit has been exceeded."""


class ExternalServiceUnavailableError(ProviderError):
    """Raised when an external provider is unavailable."""


class InvalidURLException(TrinetraException):
    """Raised when an invalid URL is provided."""


class RiskScoringError(TrinetraException):
    """Raised when risk scoring fails."""


class AIProviderError(TrinetraException):
    """Raised when the AI provider (Gemini) fails."""


class ConfigurationError(TrinetraException):
    """Raised when required configuration is missing."""