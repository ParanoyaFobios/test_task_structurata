"""
Custom exception hierarchy for the Structurata SDK.

Allows callers to distinguish between network issues,
validation errors, and general SDK failures.
"""


class StructurataSdkError(Exception):
    """Base exception class for all errors raised by this SDK."""


class ApiNetworkError(StructurataSdkError):
    """Raised when the network request fails or returns an error status code."""


class ApiValidationError(StructurataSdkError):
    """Raised when the server response fails Pydantic validation."""
