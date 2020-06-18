from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status


class JWTTest(TestCase):
    def test_jwt(self):
        user = User.objects.create(username='test_account')
        user.set_password('test_account')
        user.save()

        # 1. JWT 토큰발급
        response = self.client.post(
            '/api/token/',
            data={
                'username': 'test_account',
                'password': 'test_account'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        refresh_token = response.data['refresh']
        access_token = response.data['access']

        # 2. 발급받은 JWT Token 확인
        # 2.1 정상 JWT 토큰 입력
        response = self.client.post(
            '/api/token/verify/',
            data={
                'token': access_token,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})

        # 2.2 잘못된 JWT 토큰 입력
        response = self.client.post(
            '/api/token/verify/',
            data={
                'token': 'WRONG',
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # 3. JWT Token 갱신
        # 3.1 정상 Refresh Token 입력
        response = self.client.post(
            '/api/token/refresh/',
            data={
                'refresh': refresh_token,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_access_token = response.data['access']

        # 3.2 잘못된 Refresh Token 입력
        response = self.client.post(
            '/api/token/refresh/',
            data={
                'refresh': 'WRONG',
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # 4. 기존 JWT Token 확인 (둘다 사용가능)
        response = self.client.post(
            '/api/token/verify/',
            data={
                'token': access_token,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(
            '/api/token/verify/',
            data={
                'token': new_access_token,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
