from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):
    def test_missing_password_in_request(self):
        url = reverse("email_registration")
        data = {"email": self.email}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_email_in_request(self):
        url = reverse("email_registration")
        data = {"password": self.password}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_email_success(self):
        url = reverse("email_registration")
        data = {"email": self.email, "password": self.password}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_already_registered_email(self):
        url = reverse("email_registration")
        data = {"email": self.email, "password": self.password}
        response = self.client.post(url, data, format="json")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_login(self):
        url = reverse("email_registration")
        data = {"email": self.email, "password": self.password}
        self.client.post(url, data, format="json")

        '''
        Register first then get token
        '''

        url = reverse("token_obtain_pair")
        data = {"email": self.email, "password": self.password}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_password(self):
        url = reverse("token_obtain_pair")
        data = {"email": self.email, "password": "123456"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_missing_credentials(self):
        url = reverse("token_obtain_pair")
        data = {"email": self.email}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def setUp(self):
        self.username = "John Doe"
        self.email = "johndoe@gmail.com"
        self.password = "strongpassword"
