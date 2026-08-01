"""
DG AI Enterprise Platform
Kernel Package

This package contains the core runtime kernel modules.
"""

from .kernel import DGKernel, kernel
from .kernel_state import KernelState
from .kernel_context import KernelContext
from .kernel_events import KernelEvent, KernelEventType
from .kernel_errors import DGKernelError


__version__ = "1.0.0"


__all__ = [
    "DGKernel",
    "kernel",
    "KernelState",
    "KernelContext",
    "KernelEvent",
    "KernelEventType",
    "DGKernelError",
]
