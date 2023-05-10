from rest_framework.decorators import api_view
from .responses import EMAIL_PASSWORD_MISSING, USER_ALREADY_EXISTS, REGISTRATION_SUCCESSFUL
from .models import User

@api_view(['POST'])
def email_registration(request):
    try:
        email = request.data['email']
        password = request.data['password']
        phone = request.data['phone']
    except KeyError:
        return EMAIL_PASSWORD_MISSING
    
    try:
        User.objects.get(email=email)
        User.objects.get(phone=phone)
        return USER_ALREADY_EXISTS
    except User.DoesNotExist:
        user = User.objects.create_user(email=email, password=password, phone=phone)
        return REGISTRATION_SUCCESSFUL