# test_integration.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_user_integration(client):
    response = client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == 'User registered successfully'

    response = client.post('/authenticate', json={'username': 'testuser', 'password': 'testpassword'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'authenticated' in data
    assert data['authenticated'] is True
