from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Todo:
    """Plain data object (like a C# record) returned by the repository instead of a model."""

    id: int
    title: str
    is_done: bool
    created_at: datetime
