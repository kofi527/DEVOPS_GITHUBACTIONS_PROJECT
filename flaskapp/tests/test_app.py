from flaskapp.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert data["message"] == "Hello from DevOps Pipeline this is a clear message from the devops team!"