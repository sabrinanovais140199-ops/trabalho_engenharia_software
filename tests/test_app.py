
import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Gerenciador de Tarefas" in response.data

def test_add_task(client):
    response = client.post("/add", data={"title": "Nova Tarefa", "description": "Descricao da Nova Tarefa"})
    assert response.status_code == 302  # Redirect
    with app.app_context():
        task = Task.query.filter_by(title="Nova Tarefa").first()
        assert task is not None
        assert task.description == "Descricao da Nova Tarefa"
        assert task.status == "A Fazer"

def test_update_task(client):
    with app.app_context():
        new_task = Task(title="Tarefa para Atualizar", description="Descricao original")
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id

    response = client.post(f"/update/{task_id}", data={"title": "Tarefa Atualizada", "description": "Descricao atualizada", "status": "Em Progresso"})
    assert response.status_code == 302
    with app.app_context():
        task = Task.query.get(task_id)
        assert task.title == "Tarefa Atualizada"
        assert task.description == "Descricao atualizada"
        assert task.status == "Em Progresso"

def test_delete_task(client):
    with app.app_context():
        new_task = Task(title="Tarefa para Deletar", description="Descricao para deletar")
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id

    response = client.get(f"/delete/{task_id}")
    assert response.status_code == 302
    with app.app_context():
        task = Task.query.get(task_id)
        assert task is None
