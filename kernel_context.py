"""
DG AI Enterprise Platform
Kernel Context

Version : 1.0.0
Status  : Production Foundation
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class KernelContext:
    """
    Shared runtime context for the DG AI Kernel.
    """

    config: Any = None
    state: Any = None

    services: dict[str, Any] = field(default_factory=dict)
    managers: dict[str, Any] = field(default_factory=dict)
    registries: dict[str, Any] = field(default_factory=dict)

    runtime_data: dict[str, Any] = field(default_factory=dict)

    def register_service(self, name: str, service: Any) -> None:
        self.services[name] = service

    def get_service(self, name: str) -> Any:
        return self.services.get(name)

    def register_manager(self, name: str, manager: Any) -> None:
        self.managers[name] = manager

    def get_manager(self, name: str) -> Any:
        return self.managers.get(name)
