from rest_framework import status
from rest_framework.test import APITestCase
import json 
from rest_framework.test import APIClient
from django.test import Client
# Create your tests here.



class AccountTests(APITestCase):
    # def setUp(self):
    #     # Every test needs a client.
    #     self.client = Client()
    #     Todolist.objects.create(id = 'c99f6b4a-a60e-7a2e-7edf-e154c46b0877', eventtype = 'TestExec', status = 'Success', ruleid = '1.3.1.1', clientid = '1')

    #sucess => /getStatusOfTriggeredEvent 
    def test_success_getStatusOfTriggeredEvent(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"toDoID" : "c99f6b4a-a60e-7a2e-7edf-e154c46b0877"}  
        response = self.client.post("/v1/event/getStatusOfTriggeredEvent",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched success status")
        self.assertEqual(res['replyCode'], "success")
    
    #EmptyPayload => /getStatusOfTriggeredEvent 
    def test_emptyPayload_getStatusOfTriggeredEvent(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/event/getStatusOfTriggeredEvent",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Value Missing")
        self.assertEqual(res['replyCode'], "Fail")

    #invalid Auth Token => /getStatusOfTriggeredEvent
    def test_invalidAuth_getStatusOfTriggeredEvent(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"toDoID" : "c99f6b4a-a60e-7a2e-7edf-e154c46b0877"}
        response = self.client.post("/v1/event/getStatusOfTriggeredEvent",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Authentication Error")
        self.assertEqual(res['replyCode'], "Fail")
