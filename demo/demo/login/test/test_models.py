from django.test import TestCase
from login.models import *

class TestModels(TestCase):
    
    def set_up(self):
        # Userlogindetails 1
        self.Userlogindetails = Userlogindetails.objects.create(id = '01', usertype = 'Triggered',name='jhon doe',password='01')

    def set_up2(self):
        # Userlogindetails 1
        self.Userlogindetails2 = Userlogindetails.objects.create(id = '02',email = 'testing@test.com', usertype = 'Triggered',name='Test User',password='01')

    def test2_Userlogindetails_models(self):
        objects = Userlogindetails.objects.get(email = 'testing@test.com')
        self.assertEqual(objects.email, 'testing@test.com')
        self.assertEqual(objects.usertype, 'Triggered')
        self.assertEqual(objects.name,'Test User')
        self.assertEqual(objects.password, '01')

    def test_Userlogindetails_models(self):
        objects = Userlogindetails.objects.get(id = '01')
        self.assertEqual(objects.id, '01')
        self.assertEqual(objects.usertype, 'Triggered')
        self.assertEqual(objects.name,'jhon doe')
        self.assertEqual(objects.password, '01')