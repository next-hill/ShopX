from django.db import models
from authentication.models import User

"""
Product
ProductMedia
Order
Payment
Seller
"""

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField()
    productMSRP = models.IntegerField()
    onSale = models.BooleanField()
    salePrice = models.IntegerField()
    publish = models.BooleanField()
    quantity = models.IntegerField(default=0)
    picture = models.TextField(default="")

    def __str__(self) -> str:
        return self.productName

class ProductMedia(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    productImage = models.TextField()

    def __str__(self) -> str:
        return self.productID.productName

class ProductSize(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.productID

class Order(models.Model):
    buyer = models.TextField()
    location = models.TextField()
    paid = models.BooleanField()
    fulfilled = models.BooleanField()
    orderDate = models.DateTimeField()
    totalAmount = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.buyer} {self.orderDate}'
    
class CartItem(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    salePrice = models.IntegerField()
    total = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.orderID} {self.productID}'

class OrderItem(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.orderID

class PaymentDetail(models.Model):
    orderID = models.OneToOneField(Order, on_delete=models.CASCADE)
    amountPaid = models.IntegerField()
    all_details = models.TextField()
    
    def __str__(self) -> str:
        return self.orderID