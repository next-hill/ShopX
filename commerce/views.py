from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer, productMediaSerializer, OrderSerializer, CartItemSerializer
from .models import Product, ProductMedia, CartItem
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
    m = ProductMedia.objects.filter(productID=pk)
    media = productMediaSerializer(m, many=True).data
    data['media'] = media
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

    cart = request.data['cart']
    for item in cart: 
        data = {
            "orderID": order.id,
            "productID": item['id'],
            "quantity": item['quantity'],
            "salePrice": item['MSRP'],
            "total": item['total']
        }
        serializer = CartItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
    return Response({"message": "Order placed successfully"}, status=status.HTTP_200_OK)

# This route is not needed unless we have a custom dashboard
@api_view(['POST'])
def addMedia(request, pk):
    print(request)
    return Response({"message": "Done"}, status=status.HTTP_200_OK)
