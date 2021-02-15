from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient

# Create your tests here.
class delete_tests(APITestCase):

    # Invalid Authorization Code
    def test_invalidauth_delete_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/df/deleteFile",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGcOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Failed")


    # Successful 
    def test_validrequest_delete_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/df/deleteFile",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "File Deleted Successfully")
        self.assertEqual(res['replyCode'], "Success")
        self.assertEqual(res['status'], "Deleted")