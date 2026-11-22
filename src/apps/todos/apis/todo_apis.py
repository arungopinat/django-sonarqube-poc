import json
from dataclasses import asdict

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.todos.commands.todo_commands import (
    CompleteTodoCommand,
    CreateTodoCommand,
    GetTodoCommand,
    ListTodosCommand,
)
from apps.todos.exceptions.todo_exceptions import (
    InvalidTodoTitleError,
    TodoAlreadyDoneError,
    TodoNotFoundError,
)


def _error(message: str, status: int) -> JsonResponse:
    return JsonResponse({"error": message}, status=status)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def todos_collection(request: HttpRequest) -> JsonResponse:
    """Layer 4: validate input, call a Command, map domain exceptions to HTTP."""
    if request.method == "GET":
        return JsonResponse({"todos": [asdict(t) for t in ListTodosCommand().execute()]})

    try:
        body = json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return _error("Body must be valid JSON", 400)
    title = body.get("title")
    if not isinstance(title, str):
        return _error("'title' (string) is required", 400)

    try:
        todo = CreateTodoCommand().execute(title)
    except InvalidTodoTitleError as e:
        return _error(str(e), 400)
    return JsonResponse(asdict(todo), status=201)


@require_http_methods(["GET"])
def todo_detail(request: HttpRequest, todo_id: int) -> JsonResponse:
    try:
        return JsonResponse(asdict(GetTodoCommand().execute(todo_id)))
    except TodoNotFoundError as e:
        return _error(str(e), 404)


@csrf_exempt
@require_http_methods(["POST"])
def todo_complete(request: HttpRequest, todo_id: int) -> JsonResponse:
    try:
        return JsonResponse(asdict(CompleteTodoCommand().execute(todo_id)))
    except TodoNotFoundError as e:
        return _error(str(e), 404)
    except TodoAlreadyDoneError as e:
        return _error(str(e), 409)
