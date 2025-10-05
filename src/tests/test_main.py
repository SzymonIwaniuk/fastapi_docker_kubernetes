def test_ping(test_app):
    """Request /ping and assert the response status and JSON body."""
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
