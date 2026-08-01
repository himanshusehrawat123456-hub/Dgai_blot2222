"""
DG AI Enterprise Platform
Kernel State

Version : 1.0.0
Status  : Production Foundation
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any

from .kernel_constants import KernelStatus


@dataclass
class KernelState:
    """
    Represents the current runtime state of the DG AI Kernel.
    """

    status: KernelStatus = KernelStatus.CREATED

    started_at: datetime | None = None
    stopped_at: datetime | None = None
    last_updated: datetime = field(default_factory=datetime.utcnow)

    active_services: int = 0
    active_agents: int = 0
    active_plugins: int = 0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def update_status(self, status: KernelStatus) -> None:
        self.status = status
        self.last_updated = datetime.utcnow()

    def set_started(self) -> None:
        self.started_at = datetime.utcnow()
        self.update_status(KernelStatus.RUNNING)

    def set_stopped(self) -> None:
        self.stopped_at = datetime.utcnow()
        self.update_status(KernelStatus.STOPPED)
