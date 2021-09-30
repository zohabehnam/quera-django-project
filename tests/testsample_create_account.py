from django.test import TestCase, Client
from accounts.models import User


class TestAll(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/accounts/register/', data={
            "username": "SAliB",
            "password": "123Aa123",
            "phone": "09383833833",
            "address": "Iran Tehran",
            "gender": "M",
            "age": "19",
            "description": "Bah Bah",
            "first_name": "Seyed Ali",
            "last_name": "Babaei",
            "email": "SAliBSAliB@gmail.com"
        }, format='json')

    def test_sample_sign_up(self):
        account = User.objects.get(username='SAliB')
        self.assertEqual('SAliB', account.username)
        self.assertEqual('M', account.gender)
        self.assertEqual(19, account.age)

    def test_sample_log_in(self):
        login_response = self.client.post('/accounts/login/', data={
            "username": "SAliB",
            "password": "123Aa123"
        }, format='json')

        self.assertEqual(200, login_response.status_code)
