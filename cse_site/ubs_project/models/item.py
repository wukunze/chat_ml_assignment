from django.conf import settings
from django.contrib.auth.models import User

from ..validators import positive_number

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=(positive_number,))
    image = models.ImageField(
        upload_to='items',
    )
    SALES_TYPE_CHOICES = (
        ("b", "buy/sell"),
        ("l", "lend"),
        ("e", "exchange")
    )
    sales_type = models.CharField(
        max_length=1,
        choices=SALES_TYPE_CHOICES,
        default="b"
    )

    STATUS_CHOICES = (
        ("l", "listing"),
        ("c", "closed")
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="l"
    )

    created_at = models.DateTimeField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

