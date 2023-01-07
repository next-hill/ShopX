from django.urls import path
from .views import createProduct, viewProduct, listAllProducts

urlpatterns = [
    path('', listAllProducts, name='all-products'),
    path('create/', createProduct, name='create-product'),
    path('<str:pk>/', viewProduct, name='view-product'),
]