from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient



class uploadFileTest(APITestCase):
    
    #sucess => /uploadFileScheduler
    def test_success_uploadFileScheduler(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973"}  
        response = self.client.post("/v1/uf/uploadFileScheduler",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched databasename by scheduler")
        self.assertEqual(res['replyCode'], "Success")

    #invalid Session id => /uploadFileScheduler
    def test_invalidSessionid_uploadFileScheduler(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID": ""}     
        response = self.client.post("/v1/uf/uploadFileScheduler",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Error in fetching the data SessionMain")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /uploadFileScheduler
    def test_emptyPayload_uploadFileScheduler(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/uf/uploadFileScheduler",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Data Request Error")
        self.assertEqual(res['replyCode'], "Failed")
    
    #invalid auth token => /uploadFileScheduler
    def test_invalidAuth_uploadFileScheduler(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973"}  
        response = self.client.post("/v1/uf/uploadFileScheduler",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /uploadFileScheduler
    def test_noAuth_uploadFileScheduler(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"SessionID": "a8a0f53c-11d6-4353-a203-f0b2b55e8973"}  
        response = self.client.post("/v1/uf/uploadFileScheduler",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

    
    #sucess => /uploadFileDump
    def test_success_uploadFileDump(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                "FileType": "Excel",
                "FilePath": "C:\\EY LLP\\Excel Files\\b2c0dd78-a57c-33c3-dce0-4d65cff1f6c3\\Inventory_Goods_Receipt_Note.xlsx",
                "SheetName": "Inventory_Goods_Receipt_Note",
                "Overwrite_merge": "M",
                "DatabaseName": "DigiCube_FS_WAM",
                "TableName": "Inventory_Goods_Receipt_Note",
                "textqualifier": "",
                "rowdelimeter": "\\r\\n",
                "columndelimeter": ",",
                "numberRowToSkip": "0",
                "iscolumnnameinfirstrow": "true"
                }  
        response = self.client.post("/v1/uf/uploadFileDump",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Data Dumped Successfully")
        self.assertEqual(res['replyCode'], "Success")

    #invalid details => /uploadFileDump
    def test_invalidSessionid_uploadFileDump(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                "FileType": "RowExcel",
                "FilePath": "C:\\EY LLP\\Excel Files\\b2c0dd78-a57c-33c3-dce0-4d65cff1f6c3\\Inventory_Goods_Receipt_Note.xlsx",
                "SheetName": "Inventory_Goods_Receipt_Note",
                "Overwrite_merge": "M",
                "DatabaseName": "DigiCube_FS_WAM",
                "TableName": "Inventory_Goods_Receipt_Note",
                "textqualifier": "",
                "rowdelimeter": "\\r\\n",
                "columndelimeter": ",",
                "numberRowToSkip": "0",
                "iscolumnnameinfirstrow": "true"
                }     
        response = self.client.post("/v1/uf/uploadFileDump",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Error While Processing Excel File")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload or value missing => /uploadFileDump
    def test_emptyPayload_uploadFileDump(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                # "FileType": "Excel",
                # "FilePath": "C:\\EY LLP\\Excel Files\\b2c0dd78-a57c-33c3-dce0-4d65cff1f6c3\\Inventory_Goods_Receipt_Note.xlsx",
                "SheetName": "Inventorsy_Goods_Receipt_Note",
                "Overwrite_merge": "M",
                "DatabaseName": "DigiCube_FS_WAM",
                "TableName": "Inventory_Goods_Receipt_Note",
                "textqualifier": "",
                "rowdelimeter": "\\r\\n",
                "columndelimeter": ",",
                "numberRowToSkip": "0",
                "iscolumnnameinfirstrow": "true"
               }  
        response = self.client.post("/v1/uf/uploadFileDump",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Error Wile Dumping File")
        self.assertEqual(res['replyCode'], "Failed")
    
    #invalid auth token => /uploadFileDump
    def test_invalidAuth_uploadFileDump(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {
                "FileType": "RowExcel",
                "FilePath": "C:\\EY LLP\\Excel Files\\b2c0dd78-a57c-33c3-dce0-4d65cff1f6c3\\Inventory_Goods_Receipt_Note.xlsx",
                "SheetName": "Inventory_Goods_Receipt_Note",
                "Overwrite_merge": "M",
                "DatabaseName": "DigiCube_FS_WAM",
                "TableName": "Inventory_Goods_Receipt_Note",
                "textqualifier": "",
                "rowdelimeter": "\\r\\n",
                "columndelimeter": ",",
                "numberRowToSkip": "0",
                "iscolumnnameinfirstrow": "true"
                }
        response = self.client.post("/v1/uf/uploadFileDump",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /uploadFileDump
    def test_noAuth_uploadFileDump(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
                "FileType": "RowExcel",
                "FilePath": "C:\\EY LLP\\Excel Files\\b2c0dd78-a57c-33c3-dce0-4d65cff1f6c3\\Inventory_Goods_Receipt_Note.xlsx",
                "SheetName": "Inventory_Goods_Receipt_Note",
                "Overwrite_merge": "M",
                "DatabaseName": "DigiCube_FS_WAM",
                "TableName": "Inventory_Goods_Receipt_Note",
                "textqualifier": "",
                "rowdelimeter": "\\r\\n",
                "columndelimeter": ",",
                "numberRowToSkip": "0",
                "iscolumnnameinfirstrow": "true"
                }  
        response = self.client.post("/v1/uf/uploadFileDump",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

    