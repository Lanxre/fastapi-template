from fastapi.testclient import TestClient
from httpx import Response

def test_health_check(client: TestClient):
    """
    Given   GET /health/
    when    request
    then    response Status Code is 200 (OK)
    """
    response: Response = client.get("/v1/health/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    