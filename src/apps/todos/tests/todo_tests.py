import pytest
from django.test import Client

from apps.todos.exceptions.todo_exceptions import InvalidTodoTitleError
from apps.todos.repositories.todo_repository import TodoRepository
from apps.todos.services.todo_service import TodoService

pytestmark = pytest.mark.django_db


class TestTodoService:
    def test_blank_title_rejected(self) -> None:
        service = TodoService(TodoRepository())
        with pytest.raises(InvalidTodoTitleError):
            service.create_todo("   ")


class TestTodoApi:
    """Integration tests: real HTTP -> API -> Command -> Service -> Repository -> DB."""

    def test_create_then_complete(self) -> None:
        client = Client()
        created = client.post(
            "/api/todos/", {"title": "learn django"}, content_type="application/json"
        )
        assert created.status_code == 201
        todo_id = created.json()["id"]

        done = client.post(f"/api/todos/{todo_id}/complete/")
        assert done.status_code == 200
        assert done.json()["is_done"] is True

        again = client.post(f"/api/todos/{todo_id}/complete/")
        assert again.status_code == 409

    def test_missing_todo_is_404(self) -> None:
        assert Client().get("/api/todos/999/").status_code == 404

    def test_bad_input_is_400(self) -> None:
        response = Client().post("/api/todos/", {}, content_type="application/json")
        assert response.status_code == 400
