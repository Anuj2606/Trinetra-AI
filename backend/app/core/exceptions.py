"""
Custom exceptions used throughout the FraudShield AI backend.

Having custom exceptions allows every provider to raise meaningful,
consistent errors instead of generic Exception objects.
"""


class FraudShieldException(Exception):
    """Base exception for the FraudShield AI project."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ProviderError(FraudShieldException):
    """Raised when a provider encounters an error."""


class InvalidAPIKeyError(ProviderError):
    """Raised when an API key is invalid or missing."""


class RateLimitError(ProviderError):
    """Raised when an API rate limit has been exceeded."""


class ExternalServiceUnavailableError(ProviderError):
    """Raised when an external provider is unavailable."""


class InvalidURLException(FraudShieldException):
    """Raised when an invalid URL is provided."""


class RiskScoringError(FraudShieldException):
    """Raised when risk scoring fails."""


class AIProviderError(FraudShieldException):
    """Raised when the AI provider (Gemini) fails."""


class ConfigurationError(FraudShieldException):
    """Raised when required configuration is missing."""