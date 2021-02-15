from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
import json 
from rest_framework.test import APIClient

class api_tests(APITestCase):
    def test_success_get_client_for_selected_user_id_and_sector(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')      
        data = {"sector_id": 4}
        response = self.client.post("/v1/api/getClientForSelectedUserIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched client for selected sector id.")
        self.assertEqual(res['replyCode'], "Success")

    # Empty Sector ID
    def test_empty_sector_id_get_client_for_selected_user_id_and_sector(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')      

        response = self.client.post("/v1/api/getClientForSelectedUserIDAndSector",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 500,
            "message": "Please provide sector_id",
            "replyCode": "Fail",
            "data": {}
        })

    # Empty Payload
    def test_empty_payload_getClientForSelectedUserIDAndSector(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')      
        response = self.client.post("/v1/api/getClientForSelectedUserIDAndSector",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 500,
            "message": "Please provide sector_id",
            "replyCode": "Fail",
            "data": {}
        })

    # Incorrect Token
    def test_incorrect_token_get_client_for_selected_user_id__and_sector(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')      
        data = {"sector_id": 4}
        response = self.client.post("/v1/api/getClientForSelectedUserIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh01'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 400,
            "message": "invalid token",
            "replyCode": "Fail",
            "data": {}
        })
   
   
    def test_get_labels(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        response = self.client.post("/v1/api/getLabels",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)   
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched labels for start page tab.")
        self.assertEqual(res['replyCode'], "Success")

    # When there is no Internet Connectivity
    #     # client = APIClient()
    #     response = self.client.post("/v1/api/getLabels",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
    #     res = json.loads(response.content)   
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(res['statusCode'], 400)
    #     self.assertEqual(res['message'], "getLabels API Fail")
    #     self.assertEqual(res['replyCode'], "Fail")


   
    def test_success_get_sector_for_selected_user_id(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        response = self.client.post("/v1/api/getSectorForSelectedUserID",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)   
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched sector for selected user id.")
        self.assertEqual(res['replyCode'], "Success")

    # When there is no Internet Connectivity
    # def test_getSectorForSelectedUserID(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     # client = APIClient()
    #     res = json.loads(response.content)   
    #     response = self.client.post("/v1/api/getSectorForSelectedUserID",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(res['statusCode'], 500)
    #     self.assertEqual(res['message'], "Bad Request")
    #     self.assertEqual(res['replyCode'], "Fail")

    # Token is Incorrect
    def test_no_token_get_sector_for_selected_user_id(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        response = self.client.post("/v1/api/getSectorForSelectedUserID",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh01'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 400,
            "message": "invalid token",
            "replyCode": "Fail"
        })
  
    def test_success_get_process_for_selected_client_id_and_sector(self):
        data = { "sector_id":1, "client_id":1}
        response = self.client.post("/v1/api/getProcessForSelectedClientIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "fetched process for selected sector and client id.",
            "replyCode": "Success",
            "data": []
                })

    # When Sector ID is Empty 
    def test_sector_id_empty_get_process_for_selected_client_id_and_sector(self):
            
            response = self.client.post("/v1/api/getProcessForSelectedClientIDAndSector",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content), {
                "statusCode": 500,
                "message": "Please provide sector_id",
                "replyCode": "Fail",
                "data": {}
            })
    
    # When Client ID is not Provided 
    def test_client_id_empty_get_process_for_selected_client_id_and_sector(self):
            
            data = { "sector_id":1}
            response = self.client.post("/v1/api/getProcessForSelectedClientIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content), {
                "statusCode": 500,
                "message": "Please provide client_id",
                "replyCode": "Fail",
                "data": {}
            })
            
    # When Sector ID is not Provided 
    def test_sector_id_empty_get_process_for_selected_client_id_and_sector_1(self):
            
            data = {"client_id":1}
            response = self.client.post("/v1/api/getProcessForSelectedClientIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content), {
                "statusCode": 500,
                "message": "Please provide sector_id",
                "replyCode": "Fail",
                "data": {}
            })
    
    # For Correct Data 
    def test_success_get_current_database(self):
            
            data = {"client_id":1}
            response = self.client.post("/v1/api/getCurrentDatabase",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            res = json.loads(response.content)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(res['statusCode'], 200)
            self.assertEqual(res['message'], "fetched current database")
            self.assertEqual(res['replyCode'], "Success")
         
    # For Empty Client ID
    def test_empty_client_id_get_current_database(self):
            
           
            response = self.client.post("/v1/api/getCurrentDatabase",format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content), {
                "statusCode": 500,
                "message": "Please provide client_id",
                "replyCode": "Fail",
                "data": {}
            })
                     
    # For No Data
    def test_no_data_get_current_database(self):
            
            data = {}
            response = self.client.post("/v1/api/getCurrentDatabase",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content), {
                "statusCode": 500,
                "message": "Please provide client_id",
                "replyCode": "Fail",
                "data": {}
            })

    
    #sucess => /getSelectTestForSelectedSubprocessID
    def test_success_get_select_test_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name": "DigiCube_FS_WAM", "risk_id": "r3,r4,r1"}  
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched test for selected sub process id"  )
        self.assertEqual(res['replyCode'], "Success")

    #invalid or database name or subprocess_id => /getSelectTestForSelectedSubprocessID
    def test_invalid_db_and_subid_get_select_test_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name": "", "risk_id": ""}  
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "invalid subprocess id."  )
        self.assertEqual(res['replyCode'], "Fail")

    #empty payload => /getSelectTestForSelectedSubprocessID
    def test_empty_payload_get_select_test_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "invalid database name or subprocess id"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getSelectTestForSelectedSubprocessID
    def test_invalidAuth_get_select_test_for_selected_subprocessid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name": "DigiCube_FS_WAM", "risk_id": "r3,r4,r1"}  
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getSelectTestForSelectedSubprocessID
    def test_noAuth_get_select_test_for_selected_subprocessid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name": "DigiCube_FS_WAM", "risk_id": "r3,r4,r1"} 
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    
    #sucess => /getTestParameterForSelectedRuleID
    def test_success_get_test_parameter_for_selected_ruleid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id": "'1.3.1.1'"}  
        response = self.client.post("/v1/api/getTestParameterForSelectedRuleID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched Test Parameter for selected rule id"  )
        self.assertEqual(res['replyCode'], "Success")

    #invalid rule id => /getTestParameterForSelectedRuleID
    def test_invalid_ruleid_get_test_parameter_for_selected_ruleid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id": "'No Id'"}    
        response = self.client.post("/v1/api/getTestParameterForSelectedRuleID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "invalid rule id."  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt or no rule id payloads => /getTestParameterForSelectedRuleID
    def test_empty_payload_get_test_parameter_for_selected_ruleid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getTestParameterForSelectedRuleID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "provide rule_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getTestParameterForSelectedRuleID
    def test_invalidAuth_get_test_parameter_for_selected_ruleid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id": "'1.3.1.1'"}  
        response = self.client.post("/v1/api/getTestParameterForSelectedRuleID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getTestParameterForSelectedRuleID
    def test_noAuth_get_test_parameter_for_selected_ruleid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id": "'1.3.1.1'"}  
        response = self.client.post("/v1/api/getTestParameterForSelectedRuleID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")


    #sucess => /getSubprocessForSelectedClientIDAndProcessID
    def test_success_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched current database")
        self.assertEqual(res['replyCode'], "Success")

    #no client id => /getSubprocessForSelectedClientIDAndProcessID
    def test_no_clientid_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"process_id": "F_01"}     
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Please provide client_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no process_id => /getSubprocessForSelectedClientIDAndProcessID
    def test_no_subprocessid_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1"}     
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Please provide process_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getSubprocessForSelectedClientIDAndProcessID
    def test_empty_payload_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Please provide client_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getSubprocessForSelectedClientIDAndProcessID
    def test_invalidAuth_get_subprocess_for_selected_clientid_and_processid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getSubprocessForSelectedClientIDAndProcessID
    def test_no_auth_get_subprocess_for_selected_clientid_and_processid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

    
    #sucess => /getListOfSessionID
    def test_success_get_list_of_sessionid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1"}  
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched list of session ID for selected client id")
        self.assertEqual(res['replyCode'], "Success")

    #invalid client id => /getListOfSessionID
    def test_invalid_client_id_get_list_of_sessionid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": ""}     
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "invalid clientId")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getListOfSessionID
    def test_empty_payload_get_list_of_sessionid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "please provide clientId")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getListOfSessionID
    def test_invalid_auth_get_list_of_sessionid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getListOfSessionID
    def test_no_auth_get_list_of_sessionid(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")
    

    #sucess => /getTableDataForSelectedSubProcessID 
    def test_success_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name" : "25May2020104446","subprocess_id" : "F_02"}  
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched table data with schema of respective table name for selected sub-process id")
        self.assertEqual(res['replyCode'], "Success")

    #no database name=> /getTableDataForSelectedSubProcessID 
    def test_invalid_databaseName_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"subprocess_id" : "F_02"}   
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "please provide database_name key")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no subprocess id=> /getTableDataForSelectedSubProcessID 
    def test_invalid_subprocessid_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name" : "25May2020104446"}   
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "please provide subprocess_id key")
        self.assertEqual(res['replyCode'], "Fail")

    #invalid database name or subprocess id=> /getTableDataForSelectedSubProcessID 
    def test_invalid_subprocessid_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name" : "123","subprocess_id" : "123"}
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "invalid subprocess id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getTableDataForSelectedSubProcessID 
    def test_empty_payload_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {} 
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "please provide database_name key")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getTableDataForSelectedSubProcessID 
    def test_invalid_auth_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"database_name" : "25May2020104446","subprocess_id" : "F_02"}  
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token =>/getTableDataForSelectedSubProcessID 
    def test_noAuth_get_table_data_for_selected_sub_processid(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name" : "25May2020104446","subprocess_id" : "F_02"}  
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid token")
        self.assertEqual(res['replyCode'], "Fail")

    #sucess => /getAllTestList
    def test_success_get_alltest_list(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"session_id":"1"}
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched test list for selected session id")
        self.assertEqual(res['replyCode'], "Success")

    #invalid session id => /getAllTestList
    def test_invalid_sessionid_get_all_test_list(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"session_id":""}     
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Invalid Session Id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getAllTestList
    def test_empty_payload_get_all_test_list(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "provide Session Id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getAllTestList
    def test_invalid_auth_get_all_test_list(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getAllTestList
    def test_noAuth_get_all_test_list(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name": "Scrap_Register_MTD","client_id": "11"}  
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")


    #sucess => /getCaptionsOfColumnMapping
    def test_success_get_captions_of_column_mapping(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name": "Scrap_Register_MTD","client_id": "11"}  
        response = self.client.post("/v1/api/getCaptionsOfColumnMapping",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched column mapping detail for selected table name.")
        self.assertEqual(res['replyCode'], "Success")

    #invalid table name id => /getCaptionsOfColumnMapping
    def test_invalid_table_name_get_captions_of_column_mapping(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name": "sssss","client_id": "11"}     
        response = self.client.post("/v1/api/getCaptionsOfColumnMapping",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "column mapping detail not available for selected table name.")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getCaptionsOfColumnMapping
    def test_empty_payload_get_captions_of_column_mapping(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getCaptionsOfColumnMapping",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Provide table name")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getCaptionsOfColumnMapping
    def test_invalid_auth_get_captions_of_column_mapping(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"table_name": "Scrap_Register_MTD","client_id": "11"}  
        response = self.client.post("/v1/api/getCaptionsOfColumnMapping",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getCaptionsOfColumnMapping
    def test_no_auth_get_caption_of_column_mapping(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name": "Scrap_Register_MTD","client_id": "11"}  
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")


    #sucess => /getColumnMappingForSelectedTable
    def test_success_get_column_mapping_for_selected_table(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"Scrap_Register_MTD"}  
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched column mapping detail for selected table name.")
        self.assertEqual(res['replyCode'], "Success")

    #invalid table name id => /getColumnMappingForSelectedTable
    def test_invalid_table_name_get_column_mapping_for_selected_table(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"sdsdsdsd"}     
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "column mapping detail not available for selected table name.")
        self.assertEqual(res['replyCode'], "Fail")
    
    #empyt payload => /getColumnMappingForSelectedTable
    def test_empty_payload_get_column_mapping_for_selected_table(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "provide table name")
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getColumnMappingForSelectedTable
    def test_invalid_auth_get_column_mapping_for_selected_table(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"table_name":"Scrap_Register_MTD"}  
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getColumnMappingForSelectedTable
    def test_noAuth_get_column_mapping_for_selected_table(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"Scrap_Register_MTD"}  
        response = self.client.post("/v1/api/getColumnMappingForSelectedTable",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")

    # Bug Test 01 For Correct Data in getCurrentDatabase
    def test_success_get_current_database(self):
            data = {"client_id":1}
            response = self.client.post("/v1/api/getCurrentDatabase",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
            res = json.loads(response.content)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(res['statusCode'], 200)
            self.assertEqual(res['message'], "fetched current database")
            self.assertEqual(res['replyCode'], "Success")
    
    #new Bug Test For Success => /getSubprocessForSelectedClientIDAndProcessID
    def test_success_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1", "process_id": "F_01"}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched sub-process for selected client id and process id.")
        self.assertEqual(res['replyCode'], "Success")

    #new Bug 01 success => /getListOfSessionID
    def test_success_get_list_of_sessionid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "1"}  
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched list of session ID for selected client id")
        self.assertEqual(res['replyCode'], "Success")

    #Bug 02 for =>getSubprocessForSelectedClientIDAndProcessID
    def test_success_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "4", "process_id": "IP_01"}  
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched sub-process for selected client id and process id.")
        self.assertEqual(res['replyCode'], "Success")
 
    #bug 01 for /getAllTestList
    def test_success_get_subprocess_for_selected_clientid_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "no id", "process_id": "no id"}  
        response = self.client.post("/v1/api/getAllTestList",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "No Content")
        self.assertEqual(res['replyCode'], "Success")

    #sucess => /saveColumnMappingsOnMappingMain
    def test_success_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"TradeDump","sector_id":"1","client_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}  
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "column mapping is inserted")
        self.assertEqual(res['replyCode'], "Success")

    #no column_mapping_list => /saveColumnMappingsOnMappingMain
    def test_no_column_mapping_list_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"TradeDump","sector_id":"1","client_id":"1"}
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide column_mapping_list")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no client Id => /saveColumnMappingsOnMappingMain
    def test_no_client_id_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"TradeDump","sector_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide client_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no sector_id => /saveColumnMappingsOnMappingMain
    def test_no_sector_id_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"TradeDump","client_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide sector_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no table_name => /saveColumnMappingsOnMappingMain
    def test_no_table_name_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data ={"sector_id":"1","client_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide table_name")
        self.assertEqual(res['replyCode'], "Fail")

    #invalid auth token => /saveColumnMappingsOnMappingMain
    def test_invalid_auth_save_column_mappings_on_mapping_Main(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"table_name":"TradeDump","sector_id":"1","client_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}  
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /saveColumnMappingsOnMappingMain
    def test_no_auth_save_column_mappings_on_mapping_main(self):
        client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"table_name":"TradeDump","sector_id":"1","client_id":"1","column_mapping_list":[{"ExcelColumnCaption":"mfund_deal_id","SQLColumnCaption":"mfund_deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"deal_id","SQLColumnCaption":"deal_id","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Exchange/ OTC","SQLColumnCaption":"Exchange/ OTC","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type","SQLColumnCaption":"Type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"broker","SQLColumnCaption":"broker","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trader","SQLColumnCaption":"Trader","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade reviewer","SQLColumnCaption":"Trade reviewer","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Trade Date","SQLColumnCaption":"Trade Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Allcation Date","SQLColumnCaption":"Allcation Date","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Fund Name","SQLColumnCaption":"Fund Name","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Security Code","SQLColumnCaption":"Security Code","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Type of security","SQLColumnCaption":"Type of security","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Sector","SQLColumnCaption":"Sector","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"PM","SQLColumnCaption":"PM","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"tran_type","SQLColumnCaption":"tran_type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"quantity","SQLColumnCaption":"quantity","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"price","SQLColumnCaption":"price","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"brk_commn","SQLColumnCaption":"brk_commn","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Total Value","SQLColumnCaption":"Total Value","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"account","SQLColumnCaption":"account","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Error type","SQLColumnCaption":"Error type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Approval taken","SQLColumnCaption":"Approval taken","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach type","SQLColumnCaption":"Breach type","TableName":"TradeDump","CustomerCode":"1","IsActive":1},{"ExcelColumnCaption":"Breach Reason","SQLColumnCaption":"Breach Reason","TableName":"TradeDump","CustomerCode":"1","IsActive":1}]}  
        response = self.client.post("/v1/upsert/saveColumnMappingsOnMappingMain",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #sucess => /updateStatusPendingForSelectedID 
    def test_success_update_status_pending_for_selectedid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_ids":["0178f5f9-be9d-5842-5eb5-2ffc0c68398b"]}  
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Set Status Pending for selected Test ID")
        self.assertEqual(res['replyCode'], "Success")
    
    #Invalid ID => /updateStatusPendingForSelectedID 
    def test_invalid_id_update_status_pending_for_selectedid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_ids":["123123-be9d-5842-5eb5-2ffc0c68398b"]}  
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Unable to set status pending for selected test id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #EmptyPayload Or No test id => /updateStatusPendingForSelectedID 
    def test_empty_payload_update_status_pending_for_selectedid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide test_id")
        self.assertEqual(res['replyCode'], "Fail")

    #invalid Auth Token => /updateStatusPendingForSelectedID
    def test_invalid_auth_update_status_pending_for_electedid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"test_ids":["0178f5f9-be9d-5842-5eb5-2ffc0c68398b"]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no Auth Token => /updateStatusPendingForSelectedID
    def test_no_auth_update_status_pending_for_selectedid(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_ids":["0178f5f9-be9d-5842-5eb5-2ffc0c68398b"]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")

    #sucess => /updateTestParameterDetail 
    def test_success_update_test_parameter_detail(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_parameter_details":[{"ID": "12", "Value": "01-Mar-2020", "RuleDetailsID": "SA_3","SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}, {"ID": "13", "Value": "31-Mar-2020", "RuleDetailsID": "SA_3", "SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Test parameter is updated")
        self.assertEqual(res['replyCode'], "Success")
    
    #no test_parameter_details id => /updateTestParameterDetail 
    def test_no_test_parameter_details_update_test_parameter_detail(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please Provid valid details")
        self.assertEqual(res['replyCode'], "Fail")
    
    #incorrect test_parameter_details values => /updateTestParameterDetail 
    def test_empty_payload_update_test_parameter_detail(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_parameter_details":[{"uid": "12", "Value": "01-Mar-2020", "RuleDetailsID": "SA_3","SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}, {"uid": "13", "Value": "31-Mar-2020", "RuleDetailsID": "SA_3", "SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "Test parameter is updated")
        self.assertEqual(res['replyCode'], "Success")

    #invalid Auth Token => /updateTestParameterDetail
    def test_invalid_auth_update_testParameter_detail(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"test_parameter_details":[{"uid": "12", "Value": "01-Mar-2020", "RuleDetailsID": "SA_3","SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}, {"uid": "13", "Value": "31-Mar-2020", "RuleDetailsID": "SA_3", "SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no Auth Token => /updateTestParameterDetail
    def test_no_auth_update_test_parameter_detail(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"test_parameter_details":[{"uid": "12", "Value": "01-Mar-2020", "RuleDetailsID": "SA_3","SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}, {"uid": "13", "Value": "31-Mar-2020", "RuleDetailsID": "SA_3", "SessionID": "5fd82c23-10fe-4d9f-9e46-f90ec98f55b2", "SessionDetailID": null}]}
        response = self.client.post("/v1/upsert/updateStatusPendingForSelectedID",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")
    

    #sucess => /getPowerBIURL 
    def test_success_getpowerbiurl(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id":"1.1.1.1"}
        response = self.client.post("/v1/api/getPowerBIURL",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched powerbi url for selected rule id.")
        self.assertEqual(res['replyCode'], "Success")
    
    #no rule_id => /getPowerBIURL 
    def test_no_test_parameter_details_get_powerbiurl(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/updateStatusPendingForSelectedID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide rule_id")
        self.assertEqual(res['replyCode'], "Fail")
    
    #incorrect rule_id values => /getPowerBIURL 
    def test_empty_payload_get_powerbiurl(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id":"1.1.1.1"}
        response = self.client.post("/v1/api/getPowerBIURL",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Value Missing")
        self.assertEqual(res['replyCode'], "Fail")

    #invalid Auth Token => /getPowerBIURL
    def test_invalid_auth_get_powerbiurl(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1')
        data = {"rule_id":"1.1.1.1"}
        response = self.client.post("/v1/api/getPowerBIURL",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no Auth Token => /getPowerBIURL
    def test_no_auth_get_powerbiurL(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"rule_id":"1.1.1.1"}
        response = self.client.post("/v1/api/getPowerBIURL",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")


    #bug test case for => /getClientForSelectedUserIDAndSector
    def test_success_get_client_for_selected_userid_and_sector(self):
        """
        Ensure we can create a new account object.
        """
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')      
        data = {"sector_id": 4}
        response = self.client.post("/v1/api/getClientForSelectedUserIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched client for selected sector id.")
        self.assertEqual(res['replyCode'], "Success")

    #for Api getTableDataForDateRange =====>>>>>>>> Count 8
    # sucess test case for => /getTableDataForDateRange
    def test_success_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched status for records"  )
        self.assertEqual(res['replyCode'], "Success")

    #database_name not present => /getTableDataForDateRange
    def test_no_database_name_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide database_name"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #table_name not present => /getTableDataForDateRange
    def test_no_table_name_get_table_Data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide table_name"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #start_date not present => /getTableDataForDateRange
    def test_no_start_date_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide start_date"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #end_date not present => /getTableDataForDateRange
    def test_no_end_date_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide end_date"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #column_name not present => /getTableDataForDateRange
    def test_no_columne_name_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide end_date"  )
        self.assertEqual(res['replyCode'], "Fail")

    #empty payload => /getTableDataForDateRange
    def test_empty_payload_get_table_data_for_date_range(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "provide database_name"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getTableDataForDateRange
    def test_invalid_auth_get_table_data_for_date_range(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getTableDataForDateRange
    def test_no_auth_get_table_data_for_date_range(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"start_date": "2018-12-15", "end_date": "2019-01-25", "database_name": "DigiCube_FS_WAM", "table_name": "ChangeMgmt_List", "column_name": "Trade Date"}  
        response = self.client.post("/v1/api/getTableDataForDateRange",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")

    #empty payload => /getRiskControlsForSelectedSubprocessId
    def test_emptyPayload_get_risk_controls_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {}  
        response = self.client.post("/v1/api/getRiskControlsForSelectedSubprocessId",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 500)
        self.assertEqual(res['message'], "Error in getRiskControlsForSelectedSubprocessId API"  )
        self.assertEqual(res['replyCode'], "Fail")
    
    #invalid auth token => /getRiskControlsForSelectedSubprocessId
    def test_invalid_auth_get_risk_controls_for_selected_subprocessid(self):
        data = {
            "subprocess_id": [
                "WAM_03_1",
                "WAM_03_10",
                "WAM_03_2",
                "WAM_03_3",
                "WAM_03_4",
                "WAM_03_5",
                "WAM_03_6",
                "WAM_03_7",
                "WAM_03_8",
                "WAM_03_9"
            ]
        }
        response = self.client.post("/v1/api/getRiskControlsForSelectedSubprocessId",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh1'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "invalid Token")
        self.assertEqual(res['replyCode'], "Fail")
    
    #no auth token => /getRiskControlsForSelectedSubprocessId
    def test_no_auth_get_risk_controls_for_selected_subprocessid(self):
        data = {
            "subprocess_id": [
                "WAM_03_1",
                "WAM_03_10",
                "WAM_03_2",
                "WAM_03_3",
                "WAM_03_4",
                "WAM_03_5",
                "WAM_03_6",
                "WAM_03_7",
                "WAM_03_8",
                "WAM_03_9"
            ]
        }  
        response = self.client.post("/v1/api/getRiskControlsForSelectedSubprocessId",data,format = 'json', **{})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 400)
        self.assertEqual(res['message'], "Please provide valid Token")
        self.assertEqual(res['replyCode'], "Fail")

    # sucess test case for => /getRiskControlsForSelectedSubprocessId
    def test_success_get_risk_controls_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "subprocess_id": [
                "WAM_03_1",
                "WAM_03_10",
                "WAM_03_2",
                "WAM_03_3",
                "WAM_03_4",
                "WAM_03_5",
                "WAM_03_6",
                "WAM_03_7",
                "WAM_03_8",
                "WAM_03_9"
            ]
        }
        response = self.client.post("/v1/api/getRiskControlsForSelectedSubprocessId",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched status for records"  )
        self.assertEqual(res['replyCode'], "Success")

    # sucess test case for => /getRiskControlsForSelectedSubprocessId
    # Changes done in response payload --> Now sending Parent Risk ID alo 
    def test_success_get_risk_controls_for_selected_subprocessid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {
            "subprocess_id": [
                "WAM_03_1",
                "WAM_03_10",
                "WAM_03_2"
            ]
        }
        response = self.client.post("/v1/api/getRiskControlsForSelectedSubprocessId",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched status for records"  )
        self.assertEqual(res['replyCode'], "Success")
         
class bug_api_test(APITestCase):
    #1 bug test sucess => /getSubprocessForSelectedClientIDAndProcessID
    def test_bug1_success_get_subprocess_for_selected_client_id_and_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"client_id": "6", "process_id": "WAM_03"}
        response = self.client.post("/v1/api/getSubprocessForSelectedClientIDAndProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched current database")
        self.assertEqual(res['replyCode'], "Success")
    
    #1 bug test sucess => /getProcessForSelectedClientIDAndSector 
    def test_bug1_success_get_process_for_selected_clientid_and_sector(self):
        data = { "sector_id":1, "client_id":6}
        response = self.client.post("/v1/api/getProcessForSelectedClientIDAndSector",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "fetched process for selected sector and client id.",
            "replyCode": "Success"
                })

    #1bug test success => /getSelectTestForSelectedSubprocessID
    def test_bug1_success_get_select_test_for_selected_subprocessid(self):
        data = {"database_name": "DigiCube_FS_WAM","risk_id": "r3,r4,r1"}
        response = self.client.post("/v1/api/getSelectTestForSelectedSubprocessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "fetched test for selected sub process id",
            "replyCode": "Success"
                })
    
    #1bug test success => /getLabels
    def test_bug1_success_get_labels(self):
        data = {}
        response = self.client.post("/v1/api/getLabels",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "fetched labels for start page tab.",
            "replyCode": "Success"
                })
    
    #2bug test invalid token => /getLabels
    def test_bug2_invalid_token_get_labels(self):
        data = {}
        response = self.client.post("/v1/api/getLabels",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0ss'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 400,
            "message": "Invalid token",
            "replyCode": "Success"
                })
    
    #3bug test no auth => /getLabels
    def test_bug3_no_token_get_labels(self):
        data = {}
        response = self.client.post("/v1/api/getLabels",data,format = 'json', **{})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 400,
            "message": "Please provide valid token",
            "replyCode": "Success"
                })

    #Bug For getListOFSessionId 8/25/2020 == 1 == http://52.152.165.57:8000/v1/api/getListOfSessionID
    def bug_test_success_get_list_of_session_id_api(self):
        data = {"client_id":"6"}
        response = self.client.post("/v1/api/getListOfSessionID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "statusCode": 200,
            "message": "fetched list of session ID for selected client id",
            "replyCode": "Success"
                })

    #Bug For getTableDataForSelectedSubProcessID 8/25/2020 == 1 == http://52.152.165.57:8000/v1/api/getTableDataForSelectedSubProcessID
    def test_Bug_1_success_get_tabledata_for_selected_sub_processid(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0')
        data = {"database_name":"August242020070118","subprocess_id":["WAM_03_1"],"risk_id":["r1"],"rule_id":["1.3.1.1","1.3.1.2","1.3.1.3","1.3.1.4"]}  
        response = self.client.post("/v1/api/getTableDataForSelectedSubProcessID",data,format = 'json', **{'HTTP_AUTHORIZATION':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0'})
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['statusCode'], 200)
        self.assertEqual(res['message'], "fetched table data with schema of respective table name for selected sub-process id")
        self.assertEqual(res['replyCode'], "Success")