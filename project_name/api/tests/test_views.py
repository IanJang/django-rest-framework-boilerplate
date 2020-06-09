from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.user.save()

    def test_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

        response = self.client.get('/users/{id}/'.format(id=self.user.id))
        self.assertEqual(response.data, {
            'url': 'http://testserver/users/{id}/'.format(id=self.user.id),
            'username': 'testuser1',
            'email': '',
            'groups': []
        })
