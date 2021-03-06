from django.db import models
from django.conf import settings

class Club(models.Model):
    """Represents a Club."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "owned_clubs")
    student = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "joined_clubs")