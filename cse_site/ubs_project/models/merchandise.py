from django.db import models
from django.conf import settings

class Merchandise(models.Model):
    """Represents a Merchandise."""

    title = models.CharField(max_length = 200)
    description = models.TextField()
    value = models.DecimalField(max_digits = 15, decimal_places = 2)

    SALES_TYPE_CHOICES = (
        ("b", "buy/sell"),
        ("l", "lend"),
        ("e", "exchange")
    )
    sales_type = models.CharField(
        max_length = 1,
        choices = SALES_TYPE_CHOICES,
        default = "b"
    )

    STATUS_CHOICES = (
        ("l", "listing"),
        ("c", "closed")
    )
    status = models.CharField(
        max_length = 1, 
        choices = STATUS_CHOICES,
        default = "l"
    )

    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)