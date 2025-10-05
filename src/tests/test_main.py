from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
	"""Request /ping and assert the response status and JSON body."""
	response = client.get("/ping")
	assert response.status_code == 200
	assert response.json() == {"ping": "pong!"}