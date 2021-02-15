from django.db import models

class Student(models.Model):
    """Represents a Student/user."""
    
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 254)
    password = models.TextField()
    created_at = models.DateTimeField()
