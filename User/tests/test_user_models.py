"""
Tests for user model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    """ Test user model"""

    def test_create_user_with_email_successful(self):
        """ Test creating a user with an email is successful"""

        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual (user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""

        sample_emails = [
            ["test1@Example.com","test1@example.com"],
            ["Test2@Example.com","test2@example.com"],
            ["TEST3@EXAMPLE.com","TEST3@example.com"],
            ["test4@example.COM","test4@example.com"],
        ]
        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email,'test123')
            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raises_error(self):
        """ Test creating user without an email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_superuser(self):
        """ Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@exmaple.com',
            'test123',)
        
        self.assertEqual(user.is_superuser)
        self.assertEqual(user.is_staff)