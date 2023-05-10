from .models import Product, Order, CartItem
from rest_framework import serializers


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

# class productMediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductMedia
#         fields = ["id", "productImage"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"