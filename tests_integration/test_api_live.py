import os

import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8003")


def test_health_live():
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
