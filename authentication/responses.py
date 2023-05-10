from rest_framework.response import Response
from rest_framework import status

EMAIL_PASSWORD_MISSING = Response({"message": "please provide email, phone, and passsword"}, status=status.HTTP_400_BAD_REQUEST)

USER_ALREADY_EXISTS = Response({"message": "already exists"}, status=status.HTTP_400_BAD_REQUEST)

REGISTRATION_SUCCESSFUL = Response({"message": "registration successful"},  status=status.HTTP_201_CREATED)