from django.db import models
from store.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    adress = models.CharField(max_length=100,blank=True, null=True)
    postal_code = models.CharField(max_length=30,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sent = models.BooleanField(default=True)
    paid = models.BooleanField(default=True)

    class Meta():
        ordering =('-created_at',)

    def __str__(self):
        return "Zamówienie {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity