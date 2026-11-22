from apps.todos.repositories.todo_repository import TodoRepository
from apps.todos.services.todo_service import TodoService


class ServiceRegistry:
    """Hand-rolled DI container: one singleton instance per service.

    Identity does the same in orchestration/service_registry.py. It is the
    equivalent of services.AddSingleton<...>() in ASP.NET Core.
    """

    def __init__(self) -> None:
        self.todo_service = TodoService(TodoRepository())


service_registry = ServiceRegistry()
