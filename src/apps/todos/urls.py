from django.urls import path

from apps.todos.apis import todo_apis

urlpatterns = [
    path("todos/", todo_apis.todos_collection),
    path("todos/<int:todo_id>/", todo_apis.todo_detail),
    path("todos/<int:todo_id>/complete/", todo_apis.todo_complete),
]
