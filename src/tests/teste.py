# Importando as bibliotecas necessárias para os testes
import pytest
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho do sistema para que o Python encontre o 'app.py'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app import app # Importa a nossa aplicação Flask

# Fixture: Uma configuração que roda antes dos testes
@pytest.fixture
def client():
    """Configura um cliente de teste simulado para fazer requisições sem precisar ligar o servidor web."""
    app.config['TESTING'] = True # Ativa o modo de testes do Flask
    with app.test_client() as client:
        yield client # Retorna o cliente para ser usado na função abaixo

# Função de Teste
def test_homepage(client):
    """Testa se a página inicial está carregando com sucesso (Código HTTP 200)."""
    rv = client.get('/') # Simula um usuário acessando a rota principal '/'
    # O teste passa se o servidor responder com status 200 (OK)
    assert rv.status_code == 200