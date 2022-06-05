from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='ben',
            email='ben@test.com',
            password='testpw123',
        )
        self.assertEqual(user.username, 'ben')
        self.assertEqual(user.email, 'ben@test.com')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='hal',
            email='hal@test.com',
            password='adminpw123',
        )
        self.assertEqual(admin_user.username, 'hal')
        self.assertEqual(admin_user.email, 'hal@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
