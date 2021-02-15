from django.db import models
from .student import Student

class Club(models.Model):
    """Represents a Club."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "owned_clubs")
    student = models.ManyToManyField(Student, related_name = "joined_clubs")