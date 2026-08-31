"""Small typed sample module for workspace smoke tests."""

from dataclasses import dataclass


@dataclass(frozen=True)
class HealthStatus:
    """Represents a minimal health payload."""

    status: str
    service: str


def get_health_status(service: str = "workspace") -> HealthStatus:
    """Return a simple health status object for the given service."""
    return HealthStatus(status="ok", service=service)
