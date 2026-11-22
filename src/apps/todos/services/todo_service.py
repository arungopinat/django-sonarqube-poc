from apps.todos.datatypes.todo import Todo
from apps.todos.exceptions.todo_exceptions import (
    InvalidTodoTitleError,
    TodoAlreadyDoneError,
    TodoNotFoundError,
)
from apps.todos.repositories.todo_repository import TodoRepository

MAX_TITLE_LENGTH = 200


class TodoService:
    """Layer 2: business rules. Talks to repositories (and, in real apps, clients)."""

    def __init__(self, todo_repository: TodoRepository) -> None:
        self.todo_repository = todo_repository

    def create_todo(self, title: str) -> Todo:
        title = title.strip()
        if not title or len(title) > MAX_TITLE_LENGTH:
            raise InvalidTodoTitleError(f"Title must be 1-{MAX_TITLE_LENGTH} characters")
        return self.todo_repository.create(title)

    def get_todo(self, todo_id: int) -> Todo:
        todo = self.todo_repository.get(todo_id)
        if todo is None:
            raise TodoNotFoundError(f"Todo {todo_id} not found")
        return todo

    def list_todos(self) -> list[Todo]:
        return self.todo_repository.list_all()

    def complete_todo(self, todo_id: int) -> Todo:
        todo = self.get_todo(todo_id)
        if todo.is_done:
            raise TodoAlreadyDoneError(f"Todo {todo_id} is already done")
        self.todo_repository.mark_done(todo_id)
        return self.get_todo(todo_id)
