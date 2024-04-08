from rest_framework import serializers

from .models import Cart

class CartSerialaizers(serializers.ModelSerializer):
    model = Cart
    field = ['qty', 'product', 'user']
