from django.urls import path
from .views import createProduct, viewProduct, listAllProducts, createOrder

urlpatterns = [
    path('', listAllProducts, name='all-products'),
    path('create/', createProduct, name='create-product'),
    path('order/', createOrder, name='finish-order'),
    path('<str:pk>/', viewProduct, name='view-product'),
]