from django.db import models
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
# Defines a cart that holds a user selection
from django.utils import timezone

from ..models import Item


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    def total(self):
        cart_lines = self.lines.all()
        total = 0
        for line in cart_lines:
            total += line.total()
        return round(total, 2)

    def contains(self, item):
        # lines = Cart_line.objects.all()
        for line in self.lines.all():
            if item == line.item:
                return True
        return False

    def add(self, item_id, quantity):
        item = Item.objects.get(id=item_id)
        if (self.contains(item)):
            print("Item already in cart")
            # cart_line = self.lines.get(item=item).add(1)
        else:
            cart_line = Cart_line(cart=self, item=item, quantity=quantity)
            cart_line.save()


# Defines a line of a cart, holding product, quantity and toppings information
class Cart_line(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="lines")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def total(self):
        return round(self.item.price * self.quantity, 2)

    def add(self, quantity):
        self.quantity += quantity
        self.save()

    def updateQuantityTo(self, quantity):
        self.quantity = quantity
        self.save()


# Defines an order
class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    payTime = models.DateTimeField(default=timezone.now)

    paid = models.BooleanField( default=False)
    braintreeId = models.CharField(max_length=200, blank=True)

    def total(self):
        return round(self.cart.total(), 2)