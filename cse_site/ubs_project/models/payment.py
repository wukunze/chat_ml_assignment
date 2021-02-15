from django.db import models
from .student import Student
from .merchandise import Merchandise

class Payment(models.Model):
    """Represents a Payment made by a Student."""
    
    title = models.CharField(max_length = 200)
    description = models.TextField()
    amount = models.DecimalField(max_digits = 15, decimal_places = 2)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE)
    merchandise = models.OneToOneField(Merchandise, on_delete = models.CASCADE)