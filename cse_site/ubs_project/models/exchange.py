from django.db import models
from django.conf import settings

class Exchange(models.Model):
    """Represents an Exchange:"""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)