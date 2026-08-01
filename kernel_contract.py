"""
DG AI Enterprise Platform
Kernel Contract

Defines the interfaces that all kernel services must follow.
"""

from abc import ABC, abstractmethod
from typing import Any


class KernelService(ABC):
    """Base interface for all kernel services."""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the service."""
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """Start the service."""
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """Stop the service."""
        raise NotImplementedError

    @abstractmethod
    def health_check(self) -> bool:
        """Return True if the service is healthy."""
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """Cleanly release resources."""
        raise NotImplementedError
