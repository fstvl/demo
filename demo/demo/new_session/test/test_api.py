from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient
from new_sessionm.views import new_session


class new_session_test(APITestCase):
    #success => /newSession
    def test_success_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ProjectName":"Demo Project",
            "ClientID":"6", "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        # response = newSession.post(self,data)
        self.assertEqual(responseNewSess['statusCode'], 200)
        self.assertEqual(responseNewSess['message'], "Success")
        self.assertEqual(responseNewSess['replyCode'], "Success")
    
    #no ClientId => /newSession
    def test_noclientid_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ProjectName":"Demo Project",
            "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide ClientID")
        self.assertEqual(responseNewSess['replyCode'], "Fail")
    
    #no SessionId => /newSession
    def test_nosessionid_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ProjectName":"Demo Project",
            "ClientID":"6", "SerialNo":1,
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide SessionID")
        self.assertEqual(responseNewSess['replyCode'], "Fail")
    
    #no AuditFrom => /newSession
    def test_noauditfrom_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851","AuditTo":"2021-08-13",
            "ProjectName":"Demo Project","ClientID":"6", "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide AuditFrom")
        self.assertEqual(responseNewSess['replyCode'], "Fail")
    
    #no AuditTo => /newSession
    def test_noauditto_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "ProjectName":"Demo Project",
            "ClientID":"6", "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide AuditTo")
        self.assertEqual(responseNewSess['replyCode'], "Fail")
    
    #no serialno => /newSession
    def test_noserialno_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ProjectName":"Demo Project",
            "ClientID":"6", "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide serialno")
        self.assertEqual(responseNewSess['replyCode'], "Fail")

    #no ProjectName => /newSession
    def test_projectname_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ClientID":"6",
            "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        self.assertEqual(responseNewSess['statusCode'], 400)
        self.assertEqual(responseNewSess['message'], "provide ProjectName")
        self.assertEqual(responseNewSess['replyCode'], "Fail")

    #invalid auth token => /newSession
    def test_invalidAuth_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ClientID":"6",
            "SerialNo":1, "SessionID":"1"
            }
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /newSession
    def test_noAuth_new_session(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ClientID":"6",
            "SerialNo":1, "SessionID":"1"
                }
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

class bug_new_session_test(APITestCase):
    #1 Bug success => /newSession
    def Bug_test_success_newSession(self):
        data = { 
            "EventType":"NewSession", "ID":"bfea3716-4e77-1b69-4712-87c2cf8403851", 
            "AuditFrom":"2020-08-13", "AuditTo":"2021-08-13", "ProjectName":"Demo Project",
            "ClientID":"6", "SerialNo":1, "SessionID":"1"
            }
        newSess = new_session()
        responseNewSess = newSess.post(data)
        # response = newSession.post(self,data)
        self.assertEqual(responseNewSess['statusCode'], 200)
        self.assertEqual(responseNewSess['message'], "Success")
        self.assertEqual(responseNewSess['replyCode'], "Success")

class view_past_result_api_tests(APITestCase):
    # 1 ====>>>>> 52.152.165.57:8000/v1/api/viewResults
    def test_success_view_past_result_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID":"1"}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Success")
        self.assertEqual(res['replyCode'], "Success")

    #2 no Session Value ====>>>>> 52.152.165.57:8000/v1/api/viewResults
    def test_nosessionvalue_view_past_result_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID":""}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "No Records Found")
        self.assertEqual(res['replyCode'], "Fail")
    
    #3 no Session Key ====>>>>> 52.152.165.57:8000/v1/api/viewResults
    def test_nosessionkey_view_past_result_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid SessionID")
        self.assertEqual(res['replyCode'], "Fail")

    #4 invalid Auth TOken ====>>>>> 52.152.165.57:8000/v1/api/viewResults
    def test_nosessionkey_view_past_result_api(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID":"1"}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #5 No Auth Token ====>>>>> 52.152.165.57:8000/v1/api/viewResults
    def test_nosessionkey_view_rast_result_api(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID":"1"}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    # 1 Bug ====>>>>> 52.152.165.57:8000/v1/api/viewResults == createdDate added
    def Bug_test_success_view_past_result_api(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID":"1"}
        response = self.client.post("/v1/api/viewResults",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Success")
        self.assertEqual(res['replyCode'], "Success")