from .models import Product, Order, CartItem, OrderItem
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

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"