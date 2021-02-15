from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.request import Request
from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_response import create_failure, create_success
from .models import Userlogindetails
from common_files.jwt_token import make_jwt_token, verify_jwt_token
import json
import requests
from rest_framework.request import HttpRequest, Request
import datetime

# Create your views here.
class login_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        """
        :param request:
        :return:
        """
        return JsonResponse({})
    
    def post(self, request: Request) -> JsonResponse:
        """
        :param request: Client request containing request information
        :return:
        """
        try:
            emailid = request.data['email']
            user_password = request.data['password']
        except Exception as e:
            self.logger.error("Error in email address or password."+str(e))
            return JsonResponse(create_failure(500, 'Value Missing', 'Fail'))
        if len(emailid) < 1:
            self.logger.error("Error in email address.")
            return JsonResponse(create_failure(401, 'Incorrect Email Address', 'Fail'))
        try:
            userInfo = Userlogindetails.objects.get(emailaddress=emailid)
        except Exception as e:
            self.logger.error("Error in Email Address."+str(e))
            return JsonResponse(create_failure(401, 'Email not found', 'Fail'))
        try:
            if str(userInfo.password) == (user_password):
                try:
                    jwtToken = make_jwt_token(data={'userid':userInfo.id})
                    outputDict = {
                        'Email': userInfo.emailaddress,
                        'Password': userInfo.password,
                        'UserID': userInfo.id,
                        'Token': jwtToken
                    }
                    output = create_success('Authorization Successful!', outputDict)
                except Exception as e:
                    self.logger.error("Error while connecting to POST API of Login Module."+str(e))
                    return JsonResponse(create_failure(401, 'Authorization Failed', 'Fail'))
            else:
                return JsonResponse(create_failure(401, 'Incorrect Password', 'Fail'))
        except Exception as e:
            self.logger.error("Error while connecting to POST API of Login Module."+str(e))
            return JsonResponse(create_failure(401, 'Authorization Failed', 'Fail'))
        return JsonResponse(output)


class change_password(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message": "Method Get Is Not Allowed While APi is working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])   
            if userid == 0:
                self.logger.error("Error in changePassword API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in changePassword API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            email = request.data['email']
            if not email:
                self.logger.error("invalid email")
                return JsonResponse(create_failure(400, 'provide valid email', 'Fail'))
        except Exception as e:
            self.logger.error("invalid email"+str(e))
            return JsonResponse(create_failure(400, 'provide email', 'Fail'))
        try:
            oldPassword = request.data['old_password']
            if not oldPassword:
                self.logger.error("invalid password")
                return JsonResponse(create_failure(400, 'provide valid old password', 'Fail'))
            userInfo = Userlogindetails.objects.get(emailaddress=email)
            self.logger.info(userInfo.password)
            if userInfo.password != (oldPassword):
                self.logger.error("invalid password")
                return JsonResponse(create_failure(400, 'invalid old password', 'Fail'))
        except Exception as e:
            self.logger.error("invalid password."+str(e))
            return JsonResponse(create_failure(400, 'provide valid old password', 'Fail'))
        try:
            newPassword = request.data['new_password']
            if not newPassword:
                self.logger.error("invalid new password")
                return JsonResponse(create_failure(400, 'provide valid new password', 'Fail'))
        except Exception as e:
            self.logger.error("invalid new password"+str(e))
            return JsonResponse(create_failure(400, 'provide valid new password', 'Fail'))
        try:
            if newPassword == oldPassword:
                self.logger.error("old password and new password should not be same")
                return JsonResponse(create_failure(400, 'old password and new password should not be same', 'Fail'))
        except Exception as e:
            self.logger.error("old password and new password should not be same"+str(e))
            return JsonResponse(create_failure(400, 'old password and new password should not be same', 'Fail'))
        try:
            currentTime = timezone.now()
            UserlogindetailsUpdate = Userlogindetails.objects.filter(
                emailaddress=email).update(password=newPassword, modifieddate=currentTime)
            if UserlogindetailsUpdate == 0:
                return JsonResponse(create_failure(204, 'Failed to update password', 'Fail'))
        except Exception as e:
            self.logger.error("invalid email" + str(e))
            return JsonResponse(create_failure(500, 'Failed to update password', 'Fail'))
        return JsonResponse(create_success("Password Updated Successfully!", []))
