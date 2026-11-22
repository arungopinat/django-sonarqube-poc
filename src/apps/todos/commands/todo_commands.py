from apps.todos.datatypes.todo import Todo
from apps.todos.service_registry import ServiceRegistry, service_registry


class BaseCommand:
    def __init__(self, registry: ServiceRegistry | None = None) -> None:
        self.service_registry = registry or service_registry


class CreateTodoCommand(BaseCommand):
    """Layer 3: orchestrates services for one use case; raises domain exceptions."""

    def execute(self, title: str) -> Todo:
        return self.service_registry.todo_service.create_todo(title)


class GetTodoCommand(BaseCommand):
    def execute(self, todo_id: int) -> Todo:
        return self.service_registry.todo_service.get_todo(todo_id)


class ListTodosCommand(BaseCommand):
    def execute(self) -> list[Todo]:
        return self.service_registry.todo_service.list_todos()


class CompleteTodoCommand(BaseCommand):
    def execute(self, todo_id: int) -> Todo:
        return self.service_registry.todo_service.complete_todo(todo_id)
