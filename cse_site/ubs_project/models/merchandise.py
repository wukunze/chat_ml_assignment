from django.db import models

class Merchandise(models.Model):
    """Represents a Merchandise."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    value = models.DecimalField(max_digits = 15, decimal_places = 2)