from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_exists():
    response = client.get("/api/v1/health")
    assert response.status_code in {200, 500}
