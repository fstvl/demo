from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from login.models import Userlogindetails
from django.test import Client
import json 

class AccountTests(APITestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        Userlogindetails.objects.create(id = 'U-1', loginid = b'0x307832434330304444444446444343383143343238444433434635414643', password = 'hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=', emailaddress = 'vikash@test.com', mbsn = b'0x307835384539433639393334344646374234433842313146464244413133')
        # and so on. for each prerequisite that should be there in db
    
    # Both Email and PAssword are correct
    def test1(self):
        """
        Ensure we can create a new account object.
        """
        data = {"email":"vikash@test.com","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "Authorization Successful!",
            "replyCode": "Success",
            "data": {
                "email": "vikash@test.com",
                "password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
                "userID": "U-1",
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0"
            }
        })

    # When Email Address is incorrect
    def test2(self):
        data = {"email":"vikkash@test.com","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 401,
            "message": "Email not found",
            "replyCode": "Fail",
            "data": {}
        })

    # When Incorrect Password
    def test3(self):
        data = {"email":"vikash@test.com","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=1"}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 401,
            "message": "Incorrect Password",
            "replyCode": "Fail",
            "data": {}
        })
  
    # When Incorrect Password
    def test4(self):
        data = {"email":"vikash@test.com","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=7"}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 401,
            "message": "Incorrect Password",
            "replyCode": "Fail",
            "data": {}
        })
  
    # When both Email address and password are incorrect
    def test5(self):
        data = {"email":"vikaash@test.com","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=1"}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 401,
            "message": "Email not found",
            "replyCode": "Fail",
            "data": {}
        })
  
    # When Password key is not provided
    def test6(self):
        data = {"email":"vikash@test.com"}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 500,
            "message": "Value Missing",
            "replyCode": "Fail",
            "data": {}
        })

    # When Email Key is not provided
    def test7(self):
        data = {"password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 500,
            "message": "Value Missing",
            "replyCode": "Fail",
            "data": {}
        })

    # Null Email Field
    def test7(self):
        data = {"email":"","password":"hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="}
        response = self.client.post("/v1/auth/login",data,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 401,
            "message": "Incorrect Email Address",
            "replyCode": "Fail",
            "data": {}
        })

    #sucess => /changePassword 
    def test_success_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0==",
            "email": "vikash@test.com",
            "old_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="
        }   
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Set Status Pending for selected Test ID")
        self.assertEqual(res['replyCode'], "Success")

    #no email => /changePassword 
    def test_no_email_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="}   
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide email")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no password => /changePassword 
    def test_no_password_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"email": "vikas@test.com"}   
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide valid new password")
        self.assertEqual(res['replyCode'], "Fail")

    #no old password => /changePassword 
    def test_no_old_password_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
            "email": "vikash@test.com"
        }
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide valid old password")
        self.assertEqual(res['replyCode'], "Fail")
        
    #invalid old password => /changePassword 
    def test_invalid_old_password_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
            "email": "vikash@test.com",
            "old_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=="
        }
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid old password")
        self.assertEqual(res['replyCode'], "Fail")

    #old password and new password are same => /changePassword 
    def test_invalid_old_password_changePassword(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
            "email": "vikash@test.com",
            "old_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="
        }
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "old password and new password should not be same")
        self.assertEqual(res['replyCode'], "Fail")


    #no auth => /changePassword
    def test_no_auth_changePassword(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
            "email": "vikash@test.com",
            "old_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="
        }   
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth => /changePassword
    def test_no_auth_changePassword(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "new_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0=",
            "email": "vikash@test.com",
            "old_password": "hmVM+wxVTpQr1aJK8aH6OfBBfdtxKOAz6vt5DRKc8I0="
        }   
        response = self.client.post("/v1/auth/change-password",data,format = 'json', **{'HTTP_AUTHORIZATION'='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0ddddd'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")