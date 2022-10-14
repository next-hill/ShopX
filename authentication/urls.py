from django.urls import path
from .views import test_request

urlpatterns = [
    path('register/', test_request, name='register_email'),
]