"""
DG AI Enterprise Platform
Enterprise Kernel

Version : 1.0.0
"""

from __future__ import annotations

import logging
from typing import Dict

from configs.project_config import config

from .kernel_constants import KernelStatus
from .kernel_context import KernelContext
from .kernel_events import KernelEvent, KernelEventType
from .kernel_errors import KernelInitializationError
from .kernel_state import KernelState


class DGKernel:
    """
    DG AI Enterprise Kernel.

    Responsible for:

    - Boot Process
    - Runtime
    - Service Registry
    - Event System
    - Lifecycle Management
    """

    def __init__(self) -> None:

        self.logger = logging.getLogger("DGKernel")

        self.config = config

        self.state = KernelState()

        self.context = KernelContext(
            config=self.config,
            state=self.state,
        )

        self.services: Dict[str, object] = {}

        self.events: list[KernelEvent] = []

        self.initialized = False

    def initialize(self) -> None:

        if self.initialized:
            return

        try:

            self.state.update_status(
                KernelStatus.INITIALIZING
            )

            self.logger.info(
                "Initializing DG AI Kernel..."
            )

            self.events.append(
                KernelEvent.create(
                    KernelEventType.KERNEL_INITIALIZING,
                    "kernel",
                )
            )

            self.initialized = True

            self.state.update_status(
                KernelStatus.CREATED
            )

            self.logger.info(
                "Kernel initialized."
            )

        except Exception as exc:

            raise KernelInitializationError(
                str(exc)
            ) from exc
            def register_service(self, name: str, service: object) -> None:
        """
        Register a service with the kernel.
        """

        if name in self.services:
            raise ValueError(f"Service '{name}' is already registered.")

        self.services[name] = service
        self.context.register_service(name, service)

        self.events.append(
            KernelEvent.create(
                KernelEventType.SERVICE_REGISTERED,
                "kernel",
                {"service": name},
            )
        )

        self.logger.info("Registered service: %s", name)

    def get_service(self, name: str) -> object:
        """
        Return a registered service.
        """

        service = self.services.get(name)

        if service is None:
            raise KeyError(f"Service '{name}' not found.")

        return service

    def start(self) -> None:
        """
        Start the DG AI Kernel.
        """

        if not self.initialized:
            self.initialize()

        self.state.set_started()

        self.events.append(
            KernelEvent.create(
                KernelEventType.KERNEL_STARTED,
                "kernel",
            )
        )

        self.logger.info("DG AI Kernel started successfully.")

    def stop(self) -> None:
        """
        Stop the DG AI Kernel.
        """

        self.state.set_stopped()

        self.events.append(
            KernelEvent.create(
                KernelEventType.KERNEL_STOPPED,
                "kernel",
            )
        )

        self.logger.info("DG AI Kernel stopped.")

    def health_check(self) -> dict:
        """
        Return current kernel health information.
        """

        return {
            "status": self.state.status.value,
            "services": len(self.services),
            "events": len(self.events),
            "initialized": self.initialized,
        } 
