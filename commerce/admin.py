from django.contrib import admin
from .models import Product, ProductMedia, Order, OrderItem, PaymentDetail, ProductSize, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentDetail)
admin.site.register(ProductSize)
admin.site.register(CartItem)
