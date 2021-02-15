from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient
from run_test.views import download_zip, run_test_api, export_test, powerbi_url

class runtest_test(APITestCase):
    
    #sucess => /runtest
    def test_success_runtest(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"ClientID":"6","RuleID":"1.3.1.1","ID":"71d05d4e-2632-7754-588a-7ff76f1225d1_1","EventType":"TestExec","SessionID":"1"}
        response = self.client.post("/v1/runtest",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Successfully ran the tests")
        self.assertEqual(res['replyCode'], "Success")
    
    #invalid auth token => /runtest
    def test_invalidAuth_runtest(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"ClientID":"6","RuleID":"1.3.1.1","ID":"71d05d4e-2632-7754-588a-7ff76f1225d1_1","EventType":"TestExec","SessionID":"1"}
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /runtest
    def test_noAuth_runtest(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"ClientID":"6","RuleID":"1.3.1.1","ID":"71d05d4e-2632-7754-588a-7ff76f1225d1_1","EventType":"TestExec","SessionID":"1"}
        response = self.client.post("/v1/mq/publishMessage",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

    
    def success_export_test(self):
        reqData = {"ClientID":"6","RuleID":"1.3.1.1","FilePath":"C:\\EY LLP\\Export Output",
        "ID":"e778ab4c-506d-8040-3441-7c751864c7da-a94","EventType":"Output","FileType":"excel","SessionID":"1"}      
        exportOutput =  exportTest.exportClass(reqData)
        self.assertEqual(exportOutput['statusCode'], 200)
        self.assertEqual(exportOutput['message'], "Export API is Working")
        self.assertEqual(exportOutput['replyCode'], "Success")

    def noruleid_export_test(self):
        reqData = {"ClientID":"6","FilePath":"C:\\EY LLP\\Export Output",
        "ID":"e778ab4c-506d-8040-3441-7c751864c7da-a94","EventType":"Output","FileType":"excel","SessionID":"1"}      
        exportOutput =  exportTest.exportClass(reqData)
        self.assertEqual(exportOutput['statusCode'], 500)
        self.assertEqual(exportOutput['message'], "API Fail due to Exception")
        self.assertEqual(exportOutput['replyCode'], "Failed")
    
    def nofiletype_export_test(self):
        reqData = {"ClientID":"6","RuleID":"1.3.1.1","FilePath":"C:\\EY LLP\\Export Output",
        "ID":"e778ab4c-506d-8040-3441-7c751864c7da-a94","EventType":"Output","SessionID":"1"}      
        exportOutput =  exportTest.exportClass(reqData)
        self.assertEqual(exportOutput['statusCode'], 500)
        self.assertEqual(exportOutput['message'], "Error in Export Test API during Fetching Ruleid Details from table")
        self.assertEqual(exportOutput['replyCode'], "Failed")
    

# Create your tests here.
class download_tests(APITestCase):

    # Invalid Authorization Code
    def test_invalidAuth_downloadAPI(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "downloadPath": [
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_1.xlsx",
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_1.csv"
        ]}
        response = self.client.post("/v1/df/download",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGcOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Invalid token")
        self.assertEqual(res['replyCode'], "Failed")


    # Successful - Valid Authorization Code and Valid Payload
    def test_validRequest_downloadAPI(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "downloadPath": [
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_1.xlsx",
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_1.csv"
        ]}
        response = self.client.post("/v1/df/download",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Zip File Created Successfully")
        self.assertEqual(res['replyCode'], "Success")

    # Empty Payload
    def test_emptyRequest_downloadAPI(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/df/download",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Failed to convert files into zip")
        self.assertEqual(res['replyCode'], "Failed")

    # Incorrect Payload
    def test_invalidRequest_downloadAPI(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "downloadPath": [
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_2.xlsx",
            "C:/inetpub/wwwroot/DownloadFiles/e9b09294-bd37-79a2-b3da-90e900dea8ab-a94/1.3.1.1_2.csv"
        ]}
        response = self.client.post("/v1/df/download",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Failed to convert files into zip")
        self.assertEqual(res['replyCode'], "Failed")


class new_run_test(APITestCase):
    #sucess  for parameter api => /runtest 
    def test_parameter_api_runtest(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = [{"ClientID":"6","RuleID":"API1","ID":"71d05d4e-2632-7754-588a-7ff76f1225d13","EventType":"TestExec","SessionID":"1"}]
        response = self.client.post("/v1/runtest",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Successfully ran the tests")
        self.assertEqual(res['replyCode'], "Success")

    #sucess for storedProcedure => /runtest 
    def test_storedProcedure_runtest(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = [{"ClientID":"6","RuleID":"BE1.1.1.01","ID":"71d05d4e-2632-7754-588a-7ff76f1225d13","EventType":"TestExec","SessionID":"1"}]
        response = self.client.post("/v1/runtest",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Successfully ran the tests")
        self.assertEqual(res['replyCode'], "Success")

    #runTest Function
    def success_run_test_fun(self):
        payload =  {"RuleID":"1.3.1.1"} #ruleId
        runTest = runTestAPI()
        responseRuntest = runTest.runTestFunction(payload)
        self.assertEqual(responseRuntest['statusCode'], 200)
        self.assertEqual(responseRuntest['message'],"Success")
        self.assertEqual(responseRuntest['replyCode'],"Success")

    #if no rule id in payload
    def noRuleId_run_test_fun(self):
        payload =  {} #ruleId
        runTest = runTestAPI()
        responseRuntest = runTest.runTestFunction(payload)
        self.assertEqual(responseRuntest['statusCode'], 500)
        self.assertEqual(responseRuntest['message'],"Please provide valid key")
        self.assertEqual(responseRuntest['replyCode'],"Fail")
    
    #if sp query not valid for rule id in payload
    def spQuery_notVal_run_test_fun(self):
        payload =  {"RuleID":"1.3.1.2"} #ruleId
        runTest = runTestAPI()
        responseRuntest = runTest.runTestFunction(payload)
        self.assertEqual(responseRuntest['statusCode'], 500)
        self.assertEqual(responseRuntest['message'],"Error in parsing ruledetails table")
        self.assertEqual(responseRuntest['replyCode'],"Failed")

    #for getAPIParameter in runTest Api
    def success_run_test_fun(self):
        payload =  {"RuleID":"API1"} #ruleId
        runTest = runTestAPI()
        responseRuntest = runTest.runTestFunction(payload)
        self.assertEqual(responseRuntest['statusCode'], 200)
        self.assertEqual(responseRuntest['message'],"Success")
        self.assertEqual(responseRuntest['replyCode'],"Success")

    #for storedProcedure in runTest Api
    def success_run_test_fun(self):
        payload =  {"RuleID":"BE1.1.1.01"} #ruleId
        runTest = runTestAPI()
        responseRuntest = runTest.runTestFunction(payload)
        self.assertEqual(responseRuntest['statusCode'], 200)
        self.assertEqual(responseRuntest['message'],"Success")
        self.assertEqual(responseRuntest['replyCode'],"Success")

class power_bi_url(APITestCase):

    #powerBi Function
    def success_url(self):
        payload =  {"ruleid":"1.1.2.1"} #ruleId
        powerBi = powerbi_url()
        responseRuntest = powerBi.powerbi(payload)
        self.assertEqual(responseRuntest['statusCode'], 200)
        self.assertEqual(responseRuntest['message'],"Success")
        self.assertEqual(responseRuntest['replyCode'],"Success")

    #if no rule id in payload
    def noruleid_run_test_fun(self):
        payload =  {"ruleid":""} #ruleId
        powerBi = powerbi_url()
        responseRuntest = powerBi.powerbi(payload)
        self.assertEqual(responseRuntest['statusCode'], 500)
        self.assertEqual(responseRuntest['message'],"Error in powerbi url Publish Message API")
        self.assertEqual(responseRuntest['replyCode'],"Fail")
    
