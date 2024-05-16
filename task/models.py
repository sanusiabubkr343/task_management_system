from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    title = models.CharField(max_length=225, null=True)
    description = models.CharField(max_length=225, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_tasks")
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ["-created_at"]
