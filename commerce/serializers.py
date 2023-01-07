from .models import Product, ProductMedia
from rest_framework import serializers


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class productMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ["id", "productImage"]