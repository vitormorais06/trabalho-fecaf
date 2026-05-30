import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# IMPORTANTE: Adicionamos o init_db na linha abaixo
from app import app, init_db 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    # IMPORTANTE: Mandamos o robô criar o banco de dados antes de iniciar o teste
    init_db() 
    with app.test_client() as client:
        yield client

def test_homepage(client):
    rv = client.get('/')
    assert rv.status_code == 200