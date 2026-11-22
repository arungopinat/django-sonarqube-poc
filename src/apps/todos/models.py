from django.db import models


class TodoModel(models.Model):
    """Django's equivalent of an EF Core entity. Only the repository touches it."""

    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "todos"
