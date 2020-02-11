from starlette.testclient import TestClient
import pytest

from main import app

@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client: TestClient):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.json() == {'status': 'ok'}


def test_entity(client: TestClient):
    data = {
        'text': 'Bagas Abisena lahir di Bandung'
    }
    resp = client.post('/entity', json=data)
    assert resp.status_code == 200
    expected = {
        "per": ["Bagas Abisena"],
        "org": [],
        "loc": ["Bandung"]
    }
    assert resp.json() == expected
