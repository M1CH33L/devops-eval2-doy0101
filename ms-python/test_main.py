import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "UP"
    assert data['service'] == "ms-python"

def test_add_endpoint(client):
    response = client.get('/api/v1/calc/add/10/15')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 25
    assert data['operation'] == "addition"