from django.core.exceptions import ValidationError


def positive_number(value):
    if value < 0.01:
        raise ValidationError('Price cannot be negative')
