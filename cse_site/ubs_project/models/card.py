from django.db import models
from django.conf import settings

class Card(models.Model):
    """Represents a debit/credit Card of a Student."""

    title = models.CharField(max_length = 200)
    description = models.TextField()

    CARD_TYPE_CHOICES = (
        ("v", "Visa"),
        ("m", "Mastercard")
    )
    card_type = models.CharField(
        max_length = 1,
        choices = CARD_TYPE_CHOICES,
        default = "v"
    )

    cardholder_name = models.CharField(max_length = 200)
    card_number = models.CharField(max_length = 16)
    security_code = models.CharField(max_length = 3)
    expiration_month = models.CharField(max_length = 2)
    expiration_year = models.CharField(max_length = 2)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)