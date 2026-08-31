from workspace_template import HealthStatus, get_health_status


def test_get_health_status_default() -> None:
    status = get_health_status()

    assert status == HealthStatus(status="ok", service="workspace")


def test_get_health_status_custom_service() -> None:
    status = get_health_status("api")

    assert status.service == "api"
    assert status.status == "ok"
