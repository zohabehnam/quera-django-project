from django.test import TestCase, Client
from accounts.models import User
from charities.models import Benefactor, Charity


class TestAll(TestCase):
    def login_account(self):
        login_response = self.client.post('/accounts/login/', data={
            "username": "SAliB",
            "password": "123Aa123"
        }, format='json')
        self.assertEqual(200, login_response.status_code)
        token = login_response.data['token']
        token = 'Token ' + token
        header = {'HTTP_AUTHORIZATION': token}
        return header

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
        self.account1 = User.objects.get(username="SAliB")

    def test_sample_benefactor_registration(self):
        header = self.login_account()
        self.client.post('/benefactors/', data={
            "experience": "2",
            "free_time_per_week": "5"
        }, format='json', **header)
        benefactor = Benefactor.objects.first()
        self.assertEqual(benefactor.user, self.account1)
        self.assertEqual(benefactor.experience, 2)

    def test_sample_charity_registration(self):
        header = self.login_account()
        self.client.post('/charities/', data={
            "name": "Mahak",
            "reg_number": "9876543210"
        }, format='json', **header)
        charity = Charity.objects.first()
        self.assertEqual(charity.name, "Mahak")
        self.assertEqual(charity.reg_number, "9876543210")
