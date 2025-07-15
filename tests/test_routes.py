from app.routes import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from SparkAI Solutions!" in response.data
