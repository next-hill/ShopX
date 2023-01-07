from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer, productMediaSerializer
from .models import Product, ProductMedia


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


from django.db.models import Count
@api_view(['POST', 'GET'])
def listAllProducts(request):
    try:
        products = Product.objects.filter(publish=True)
        data = productSerializer(products, many=True).data
        for x in data:
            m = ProductMedia.objects.filter(productID=x['id'])
            media = productMediaSerializer(m, many=True).data
            x['media'] = media

        return Response(data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response("There are no products available", status=status.HTTP_200_OK)


@api_view(['GET'])
def viewProduct(request, pk):
    data = {
        'name': 'Shoe 1',
        'price': 3000
    }
    return Response(data, status=status.HTTP_200_OK)
