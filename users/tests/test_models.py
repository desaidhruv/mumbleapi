from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import include, path, reverse , resolve
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class AccountTests(APITestCase):

    def setUp(self):
        url = reverse('users-api:register')
        data = {
            'username':'test',
            'email':'test@gmail.com', 
            'password':'test@123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.test_user = User.objects.get(username='test')
        self.test_user_pwd = 'test@123'

    def test_admin_create_account(self):
        url = reverse('users-api:register')
        data = {
            'username': 'admin',
            'email': 'admin@gmail.com',
            'password': 'admin'
        } 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)
        admin_user = User.objects.get(username='admin')
        self.assertEqual(admin_user.username,'admin')

    def test_admin_login_account(self):
        user = User.objects.create(username='admin')
        user.set_password('admin')
        user.save()
        url = reverse('users-api:login')
        data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(username='admin').username, 'admin')