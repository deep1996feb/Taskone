from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    dateadd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
