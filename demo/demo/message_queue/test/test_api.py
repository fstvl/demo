from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient
from messageQueue.views.publishMessage import sendEmail

class msg_queues_test(APITestCase):

    #sucess => /publishMessage
    def test_success_publish_message(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                "ClientID": "1",
                "EventType": "Import",
                "FilePath": "C:\\EY LLP\\Excel Files\\c92685ce-d3a2-ecea-b013-5fb217d4e19\\Inventory_Goods_Receipt_Note.xlsx",
                "FileType": "Excel",
                "ID": "04e68b80-b784-67a9-dffa-016e62adeda812345",
                "SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973",
                "Sheet_Name":"Inventory_Goods_Receipt_Note",
                "TableName": "ExceptionsTraderApprover",
                "Overwrite_Merge": "M"
                }  
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Success")
        self.assertEqual(res['replyCode'], "Success")
    
    #empyt payload => /publishMessage
    def test_emptyPayload_publish_message(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Success")
        self.assertEqual(res['replyCode'], "Success")
    
    #invalid auth token => /publishMessage
    def test_invalidAuth_publish_message(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {
                "ClientID": "1",
                "EventType": "Import",
                "FilePath": "C:\\EY LLP\\Excel Files\\c92685ce-d3a2-ecea-b013-5fb217d4e19\\Inventory_Goods_Receipt_Note.xlsx",
                "FileType": "Excel",
                "ID": "04e68b80-b784-67a9-dffa-016e62adeda812345",
                "SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973",
                "Sheet_Name":"Inventory_Goods_Receipt_Note",
                "TableName": "ExceptionsTraderApprover",
                "Overwrite_Merge": "M"
                }  
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /publishMessage
    def test_noauth_publish_message(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                "ClientID": "1",
                "EventType": "Import",
                "FilePath": "C:\\EY LLP\\Excel Files\\c92685ce-d3a2-ecea-b013-5fb217d4e19\\Inventory_Goods_Receipt_Note.xlsx",
                "FileType": "Excel",
                "ID": "04e68b80-b784-67a9-dffa-016e62adeda812345",
                "SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973",
                "Sheet_Name":"Inventory_Goods_Receipt_Note",
                "TableName": "ExceptionsTraderApprover",
                "Overwrite_Merge": "M"
                }  
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")


 class send_email_test(APITestCase ):
        #sendEmail function sj uccess 
        def success_send_email(self):
            emailIds = ['dilip.dura@celebaltech.com','vikash.choudhary@celebaltech.com']
            attachment = ['C:\inetpub\wwwroot\DownloadFiles\e778ab4c-506d-8040-3441-7c751864c7da-a94']
            sendEmailResponse = sendEmail(attachment,emailIds)
            self.assertEqual(res['statusCode'], 200)
            self.assertEqual(res['message'], "Email Sent.")
            self.assertEqual(res['replyCode'], "Success")

        #if no email id is present
        def email_cant_sent(self):
            emailIds = []
            attachment = ['C:\inetpub\wwwroot\DownloadFiles\e778ab4c-506d-8040-3441-7c751864c7da-a94']
            sendEmailResponse = sendEmail(attachment,emailIds)
            self.assertEqual(res['statusCode'], 400)
            self.assertEqual(res['message'], "Please Provide Email Id")
            self.assertEqual(res['replyCode'], "Failed")

        #if attacment is not available
        def email_cant_sent(self):
            emailIds = ['dilip.dura@celebaltech.com','vikash.choudhary@celebaltech.com']
            attachment = []
            sendEmailResponse = sendEmail(attachment,emailIds)
            self.assertEqual(res['statusCode'], 400)
            self.assertEqual(res['message'], "Email Cannot Sent")
            self.assertEqual(res['replyCode'], "Failed")

