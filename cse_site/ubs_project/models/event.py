from django.db import models
from .student import Student

class Event(models.Model):
    """Represents an Event."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE)