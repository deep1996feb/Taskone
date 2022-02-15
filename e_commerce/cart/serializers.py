from email.policy import default
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CartItem, OrderDetails

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length = 100)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required = False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

class Deliveredform(serializers.ModelSerializer):
    class Meta:
        models = OrderDetails
        fields = ('__all__')
