from django.db import models
from django.conf import settings
from django.utils import timezone

class Exchange(models.Model):
    """Represents an Exchange:"""

    title = models.CharField(max_length = 200, db_index=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)