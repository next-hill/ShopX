from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer, OrderSerializer, OrderItemSerializer
from .models import Product, CartItem, Order
from django.utils import timezone


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    data = {
        'productName': request.data['name'], 
        'productDescription': request.data['description'],
        'productMSRP': request.data['price'],
        'onSale': False,
        'salePrice': request.data['price'],
        'publish': False
    }

    serializer = productSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def listAllProducts(request):
    try:
        products = Product.objects.filter(publish=True)
        data = productSerializer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response("There are no products available", status=status.HTTP_200_OK)

@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    data = productSerializer(product).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrder(request): 

    data = {
        "buyer": request.user.email, 
        "location": request.data['location'],
        "paid": False,
        "fulfilled": False,
        "orderDate": timezone.now(),
        "totalAmount": request.data['total']
    }

    serializer = OrderSerializer(data=data)

    if serializer.is_valid():
        order = serializer.save()
    else: 
        print(serializer.errors)
        return Response({"message": "An error occured, please contact us"})

    cart = request.data['cart']

    total = 0
    for item in cart: 
        data = {
            "orderID": order.id,
            "productID": item['id'],
            "quantity": item['quantity']
        }
        product = Product.objects.get(id=item['id'])
        if product.quantity > item['quantity']:
            product.quantity = product.quantity - item['quantity']
            product.save()
        else:
            errors = "Some items are not in stock, we will contact you soon"
        data['salePrice'] = product.salePrice
        item_total = product.salePrice * item["quantity"]
        data['total'] = item_total
        serializer = OrderItemSerializer(data=data)
        if serializer.is_valid():
            total = total + item_total
            serializer.save()
        else:
            print(serializer.errors)
            return Response({"message": "An error occured, please contact us"})
    order.totalAmount = total
    order.save()
    return Response({"message": "Order placed successfully", "id": order.id}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payOrder(request, pk):
    # handle payment things here
    try:
        order = Order.objects.get(id=pk)
        order.paid = True
        order.save()
        return Response({"message": "You have successfully paid your order"})
    except Order.DoesNotExist:
        return Response({"message": "This order does not exist"})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myOrders(request):
    orders = Order.objects.filter(buyer=request.user.email)
    data = OrderSerializer(orders, many=True).data

    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def addItemToCart(request):
    # handle adding item to cart so that it can be saved to the db

    return Response({"message": "Success"})

# This route is not needed unless we have a custom dashboard
@api_view(['POST'])
def addMedia(request, pk):
    print(request)
    return Response({"message": "Done"}, status=status.HTTP_200_OK)
