import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from src.main import app  


@pytest.mark.asyncio
async def test_simple_send():
    
    test_email_data = {
        "recipients": ["unbtv20241@gmail.com"],
        "tema": "Exemplo de Tema",
        "descricao": "Exemplo de Descrição",
        "quando": "Exemplo de Quando",
        "local": "Exemplo de Local",
        "responsavel": "Exemplo de Responsável",
        "telefone_responsavel": "Exemplo de Telefone",
        "email_contato": "geraldovictor@outlook.com",
        "url_video": "https://www.youtube.com/watch?v=yTpI3blS2eE",
    }

    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/pauta/email", json=test_email_data)
    
    assert response.status_code == 200
