"""
DG AI Enterprise Platform
Kernel Events

Version : 1.0.0
Status  : Production Foundation
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


class KernelEventType(str, Enum):
    KERNEL_CREATED = "kernel.created"
    KERNEL_INITIALIZING = "kernel.initializing"
    KERNEL_INITIALIZED = "kernel.initialized"
    KERNEL_STARTING = "kernel.starting"
    KERNEL_STARTED = "kernel.started"
    KERNEL_STOPPING = "kernel.stopping"
    KERNEL_STOPPED = "kernel.stopped"
    KERNEL_FAILED = "kernel.failed"

    SERVICE_REGISTERED = "service.registered"
    SERVICE_REMOVED = "service.removed"

    CONFIG_LOADED = "config.loaded"

    HEALTH_CHECK_STARTED = "health.started"
    HEALTH_CHECK_COMPLETED = "health.completed"


@dataclass(slots=True)
class KernelEvent:
    event_type: KernelEventType
    timestamp: datetime
    source: str
    data: Dict[str, Any]

    @classmethod
    def create(
        cls,
        event_type: KernelEventType,
        source: str,
        data: Dict[str, Any] | None = None,
    ) -> "KernelEvent":
        return cls(
            event_type=event_type,
            timestamp=datetime.utcnow(),
            source=source,
            data=data or {},
        )
