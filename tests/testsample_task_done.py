from django.test import TestCase, Client
from accounts.models import User
from charities.models import Charity, Benefactor, Task


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
        header = self.login_account()
        self.client.post('/charities/', data={
            "name": "Mahak",
            "reg_number": "9876543210"
        }, format='json', **header)
        self.sample_charity = Charity.objects.get(id=1)
        self.client.post('/benefactors/', data={
            "experience": "2",
            "free_time_per_week": "4"
        }, format='json', **header)
        self.sample_benefactor = Benefactor.objects.get(id=1)
        self.sample_task1 = Task.objects.create(
            title='Sample Task 1',
            state='P',
            charity=self.sample_charity,
            description="Test Description",
        )
        self.sample_task2 = Task.objects.create(
            title='Sample Task 2',
            state='A',
            charity=self.sample_charity,
            description="Test Description",
        )

    def test_sample_task_not_assigned(self):
        header = self.login_account()
        #                            Test 1
        sample_test1 = self.client.post('/tasks/1/done/', data={}, format='json', **header)
        self.assertEqual(404, sample_test1.status_code)
        self.assertEqual({'detail': 'Task is not assigned yet.'}, sample_test1.data)

    def test_sample_task_done(self):
        header = self.login_account()
        #                            Test 2
        sample_test2 = self.client.post('/tasks/2/done/', data={}, format='json', **header)
        self.assertEqual(200, sample_test2.status_code)
        self.assertEqual({'detail': 'Task has been done successfully.'}, sample_test2.data)
        self.sample_task2.refresh_from_db()
        self.assertEqual('D', self.sample_task2.state)
