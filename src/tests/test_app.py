import pytest

@pytest.fixture
def client():
    from src.app import app  # Asegúrate de que la ruta sea correcta
    app.config.testing = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(response.json) == 2  # Asegúrate de que haya dos todos iniciales

def test_simple_add(client):
    response = client.post('/todos', json={"done": True, "label": "Sample Todo 2"})
    assert response.status_code == 201  # Asegúrate de que espera 201
    assert len(response.json) == 3  # Asegúrate de que hay tres todos después de agregar

def test_delete_todo(client):
    response = client.post('/todos', json={"done": False, "label": "Todo to be deleted"})
    assert response.status_code == 201  # Verifica que se agregó correctamente

    new_todo_index = len(response.json) - 1  # Obtén el índice del nuevo todo
    response = client.delete(f'/todos/{new_todo_index}')  # Usa el índice dinámico
    assert response.status_code == 200
    assert response.json['message'] == "Todo deleted"

    response = client.get('/todos')
    print("Todos restantes:", response.json)  # Para depuración
    assert len(response.json) == 2  # Verifica que hay 2 todos restantes
