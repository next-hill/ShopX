from django.urls import path
from .views import createProduct, viewProduct, listAllProducts, createOrder, payOrder, addItemToCart, myOrders

urlpatterns = [
    path('', listAllProducts, name='all-products'),
    path('create/', createProduct, name='create-product'),
    path('order/', createOrder, name='finish-order'),
    path('pay/<int:pk>/', payOrder, name='pay-order'),
    path('cart/add/', addItemToCart, name='add-item-cart'),
    path('orders/', myOrders, name='my-orders'),
    path('<str:pk>/', viewProduct, name='view-product'),
]