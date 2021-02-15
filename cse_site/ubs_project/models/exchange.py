from django.db import models
from .student import Student

class Exchange(models.Model):
    """Represents an Exchange:"""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE)