class TodoError(Exception):
    """Base class for all todo domain errors."""


class TodoNotFoundError(TodoError):
    pass


class InvalidTodoTitleError(TodoError):
    pass


class TodoAlreadyDoneError(TodoError):
    pass
