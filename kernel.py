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
    def dispatch_event(self, event: KernelEvent) -> None:
        """
        Process and store kernel events.
        """

        self.events.append(event)

        self.logger.debug(
            "Event dispatched: %s",
            event.event_type.value
        )


    def get_events(self) -> list[KernelEvent]:
        """
        Return all kernel events.
        """

        return self.events.copy()


    def diagnostics(self) -> dict:
        """
        Provide kernel diagnostic information.
        """

        return {
            "project": self.config.PROJECT_NAME,
            "version": self.config.VERSION,
            "status": self.state.status.value,
            "initialized": self.initialized,
            "services": list(self.services.keys()),
            "event_count": len(self.events),
            "active_services": self.state.active_services,
            "active_agents": self.state.active_agents,
            "active_plugins": self.state.active_plugins,
        }


    def reset(self) -> None:
        """
        Reset kernel runtime state.
        """

        self.services.clear()
        self.events.clear()

        self.state.active_services = 0
        self.state.active_agents = 0
        self.state.active_plugins = 0

        self.logger.warning(
            "Kernel runtime state has been reset."
        )


    def shutdown(self) -> None:
        """
        Complete kernel shutdown process.
        """

        self.events.append(
            KernelEvent.create(
                KernelEventType.KERNEL_STOPPING,
                "kernel",
            )
        )

        self.stop()

        self.logger.info(
            "DG AI Kernel shutdown completed."
        )
            def load_service(self, name: str, service: object) -> None:
        """
        Load and register a service into the kernel runtime.
        """

        self.register_service(name, service)

        self.state.active_services = len(
            self.services
        )

        self.logger.info(
            "Service loaded: %s",
            name
        )


    def remove_service(self, name: str) -> None:
        """
        Remove a service from the kernel.
        """

        if name in self.services:

            del self.services[name]

            self.state.active_services = len(
                self.services
            )

            self.events.append(
                KernelEvent.create(
                    KernelEventType.SERVICE_REMOVED,
                    "kernel",
                    {"service": name},
                )
            )

            self.logger.info(
                "Service removed: %s",
                name
            )


    def initialize_services(self) -> None:
        """
        Initialize all registered services.
        """

        for name, service in self.services.items():

            if hasattr(service, "initialize"):

                service.initialize()

                self.logger.info(
                    "Initialized service: %s",
                    name
                )


    def start_services(self) -> None:
        """
        Start all registered services.
        """

        for name, service in self.services.items():

            if hasattr(service, "start"):

                service.start()

                self.logger.info(
                    "Started service: %s",
                    name
                )


    def stop_services(self) -> None:
        """
        Stop all registered services.
        """

        for name, service in self.services.items():

            if hasattr(service, "stop"):

                service.stop()

                self.logger.info(
                    "Stopped service: %s",
                    name
                )
                    def resolve_dependencies(self) -> None:
        """
        Validate service dependencies before runtime.
        """

        for name, service in self.services.items():

            dependencies = getattr(
                service,
                "dependencies",
                []
            )

            for dependency in dependencies:

                if dependency not in self.services:

                    raise KernelInitializationError(
                        f"Missing dependency '{dependency}' "
                        f"for service '{name}'"
                    )

        self.logger.info(
            "All service dependencies resolved."
        )


    def run_health_checks(self) -> dict:
        """
        Execute health checks for registered services.
        """

        results = {}

        for name, service in self.services.items():

            if hasattr(service, "health_check"):

                results[name] = service.health_check()

            else:

                results[name] = True

        return results


    def boot(self) -> None:
        """
        Complete DG AI Kernel boot sequence.
        """

        self.initialize()

        self.resolve_dependencies()

        self.initialize_services()

        self.start_services()

        self.start()

        self.logger.info(
            "DG AI Enterprise Kernel boot completed."
        )


    def get_runtime_info(self) -> dict:
        """
        Return complete runtime information.
        """

        return {
            "project": self.config.PROJECT_NAME,
            "version": self.config.VERSION,
            "status": self.state.status.value,
            "services": list(self.services.keys()),
            "health": self.run_health_checks(),
        }
            def safe_execute(self, operation, *args, **kwargs):
        """
        Execute a kernel operation safely.
        """

        try:
            return operation(*args, **kwargs)

        except Exception as exc:

            self.events.append(
                KernelEvent.create(
                    KernelEventType.KERNEL_FAILED,
                    "kernel",
                    {
                        "error": str(exc),
                    },
                )
            )

            self.state.update_status(
                KernelStatus.FAILED
            )

            self.logger.exception(
                "Kernel operation failed."
            )

            raise


    def recover(self) -> None:
        """
        Attempt runtime recovery.
        """

        self.logger.warning(
            "Starting kernel recovery process."
        )

        self.state.update_status(
            KernelStatus.INITIALIZING
        )

        self.initialize_services()

        self.start_services()

        self.state.update_status(
            KernelStatus.RUNNING
        )

        self.logger.info(
            "Kernel recovery completed."
        )


    def summary(self) -> dict:
        """
        Return a simple kernel summary.
        """

        return {
            "name": self.config.PROJECT_NAME,
            "version": self.config.VERSION,
            "status": self.state.status.value,
            "services_count": len(self.services),
            "events_count": len(self.events),
            "initialized": self.initialized,
        }


# Global Kernel Instance
kernel = DGKernel()
    def validate(self) -> bool:
        """
        Validate kernel readiness.
        """

        checks = [
            self.config is not None,
            self.state is not None,
            self.context is not None,
            self.initialized is True,
        ]

        return all(checks)


    def ready(self) -> bool:
        """
        Check if kernel is ready for execution.
        """

        return (
            self.validate()
            and self.state.status
            in (
                KernelStatus.CREATED,
                KernelStatus.RUNNING,
            )
        )


    def export_state(self) -> dict:
        """
        Export complete kernel state.
        """

        return {
            "project": self.config.PROJECT_NAME,
            "version": self.config.VERSION,
            "status": self.state.status.value,
            "services": list(self.services.keys()),
            "events": len(self.events),
            "runtime_data": self.context.runtime_data,
        }


    def __repr__(self) -> str:
        return (
            f"<DGKernel "
            f"project={self.config.PROJECT_NAME} "
            f"status={self.state.status.value}>"
        )


__all__ = [
    "DGKernel",
    "kernel",
]
