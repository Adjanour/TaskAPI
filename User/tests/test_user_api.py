""" Tests for the user API"""

from django.test import TestCase 
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.test import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """Creae and return a new user"""

    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the public features of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful"""
        payload = {
            'email':'test@example.com',
            'password':'testpass123',
            'first_name':'test',
            'last_name':'test_lastname',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)


    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""
        payload = {
            'email':'test@example.com',
            'password':'testpass123',
            'first_name':'test',
            'last_name':'test_lastname',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)