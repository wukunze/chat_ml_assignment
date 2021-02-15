from django.db import models
from .student import Student

class Message(models.Model):
    """Represents a message sent by a Student."""

    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "sent_messages")
    student = models.ManyToManyField(Student, related_name = "received_messages")