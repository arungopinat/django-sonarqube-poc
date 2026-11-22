from apps.todos.datatypes.todo import Todo
from apps.todos.models import TodoModel


class TodoRepository:
    """Layer 1: data access only. No business rules, returns dataclasses not models."""

    def create(self, title: str) -> Todo:
        return self._to_todo(TodoModel.objects.create(title=title))

    def get(self, todo_id: int) -> Todo | None:
        model = TodoModel.objects.filter(id=todo_id).first()
        return self._to_todo(model) if model else None

    def list_all(self) -> list[Todo]:
        return [self._to_todo(m) for m in TodoModel.objects.order_by("id")]

    def mark_done(self, todo_id: int) -> None:
        TodoModel.objects.filter(id=todo_id).update(is_done=True)

    @staticmethod
    def _to_todo(model: TodoModel) -> Todo:
        return Todo(
            id=model.id,
            title=model.title,
            is_done=model.is_done,
            created_at=model.created_at,
        )
