from django.conf import settings
from django.contrib.auth.models import User

from ..validators import positive_number

from django.db import models


class Lend(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=(positive_number,))
    image = models.ImageField(
        upload_to='items',
    )

    status = models.IntegerField()

    created_at = models.DateTimeField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_id = models.IntegerField(null=True)
    rent_user_id = models.IntegerField()
    lend_user_id = models.IntegerField()

    # def __str__(self):
    #     return f'{self.name}'
