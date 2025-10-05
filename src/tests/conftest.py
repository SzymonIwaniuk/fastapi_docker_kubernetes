import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    """Create a TestClient for the FastAPI app."""
    client = TestClient(app)
    yield client
