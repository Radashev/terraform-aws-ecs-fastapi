from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200


def test_404():
    r = client.get("/no-such-page")
    assert r.status_code == 404
