from django.db import models
from django.conf import settings

class Event(models.Model):
    """Represents an Event."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return "Event(title=%s)" % self.title