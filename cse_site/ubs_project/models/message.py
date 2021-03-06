from django.db import models
from django.conf import settings

class Message(models.Model):
    """Represents a message sent by a Student."""

    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "sent_messages")
    student = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "received_messages")