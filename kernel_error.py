"""
DG AI Enterprise Platform
Kernel Errors

Version : 1.0.0
Status  : Production Foundation
"""


class DGKernelError(Exception):
    """Base exception for all kernel-related errors."""

    pass


class KernelInitializationError(DGKernelError):
    """Raised when kernel initialization fails."""

    pass


class KernelStartupError(DGKernelError):
    """Raised when kernel startup fails."""

    pass


class KernelShutdownError(DGKernelError):
    """Raised when kernel shutdown fails."""

    pass


class ConfigurationError(DGKernelError):
    """Raised when configuration is invalid."""

    pass


class ServiceRegistrationError(DGKernelError):
    """Raised when a service cannot be registered."""

    pass


class ServiceNotFoundError(DGKernelError):
    """Raised when a requested service is not found."""

    pass


class DependencyResolutionError(DGKernelError):
    """Raised when dependencies cannot be resolved."""

    pass


class RuntimeErrorDG(DGKernelError):
    """Raised when the DG AI runtime encounters an unexpected error."""

    pass


class SecurityInitializationError(DGKernelError):
    """Raised when security initialization fails."""

    pass


class PluginLoadError(DGKernelError):
    """Raised when a plugin fails to load."""

    pass


class HealthCheckError(DGKernelError):
    """Raised when a health check fails."""

    pass
