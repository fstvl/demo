################################################################################################
# views.py: Part of deleteFile Package, Used for deleting files from server
# Classes:
# Delete
#
#################################################################################################

from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import HttpRequest, Request

from common_files.read_configuration import read_config	
from common_files.jwt_token import verify_jwt_token
from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_response import create_failure, create_success

import requests,os,time,sys
from datetime import datetime

########################################################################################################
# Class Delete - Collection of functions for deleting files which are on the server
# Functions:
# post - is used to take input from the client and send response to the client.
# main_function - is used to differentiate directories and to call different functions
# file_path_creation - is used to create paths of files so that they can be individually deleted
# check_expired - is used to check if file is expired(older than 12 hours) or not
# check_empty - is used to check if folder is empty or not
# deleteFile - is used to delete file using os module
########################################################################################################

class Delete(APIView):
    def __init__(self):
        self.logger = get_logger() 
        self.config = read_config()
    def post(self,request : Request) -> JsonResponse:
        try:
            token = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if token == 0:
                self.logger.error("Error in Delete API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Failed'))
        except Exception as e:
            self.logger.error("Error in Authentication Delete API."+str(e))
            return JsonResponse(create_failure(500, 'Authentication Error', 'Failed'))

        try:
            response = self.main_function(request)
            return JsonResponse(response)
        except Exception as e:
            self.logger.error("Error in Delete API "+str(e))
            return JsonResponse(create_failure(500, 'API Fail due to Exception', 'Failed'))

    def main_function(self,request):
        try:
            ########## Excel File Delete ##########
            try:
                excelFileRoot = self.config['ENV_VARIABLE']['file_path']
                res = self.file_path_creation(request,excelFileRoot)
                if(res == False):
                    create_failure(500,"API Fail due to Exception","Failed")
            except Exception as e:
                self.logger.error("Error in Delete API "+str(e))
                return JsonResponse(create_failure(500,"API Fail due to Exception","Failed"))

            ########## Zip File Delete ##########
            try:
                zipFileRoot = self.config['ENV_VARIABLE']['file_path_zip']
                res = self.file_path_creation(request,zipFileRoot)
                if(res == False):
                    create_failure(500,"API Fail due to Exception","Failed")
            except Exception as e:
                self.logger.error("Error in Delete API "+str(e))
                return JsonResponse(create_failure(500,"API Fail due to Exception","Failed"))

            ########## Download File Delete ##########
            try:
                downloadFileRoot = self.config['ENV_VARIABLE']['file_path_download']
                res = self.file_path_creation(request,downloadFileRoot)
                if(res == False):
                    create_failure(500,"API Fail due to Exception","Failed")
            except Exception as e:
                self.logger.error("Error in Delete API "+str(e))
                return JsonResponse(create_failure(500,"API Fail due to Exception","Failed"))
            return create_success('File Deleted Successfully','Deleted')
        except Exception as e:
            self.logger.error("Error in Delete API "+str(e))
            return JsonResponse(create_failure(500,"API Fail due to Exception","Failed"))

    def file_path_creation(self,request,root):
        try:
            for path,subdirs,files in os.walk(root):
                for file in files:
                    filePath = os.path.join(path, file)
                    self.logger.info("{} is in process".format(filePath))
                    time = os.path.getmtime(filePath)
                    if(self.check_expired(time)):
                        self.logger.info("{} is expired".format(filePath))
                        res = self.deleteFile(filePath,path)
            return True
        except Exception as e:
            self.logger.error("Error in Delete API "+str(e))
            return False

    def check_expired(self,mtime):
        try:
            currentTime = datetime.now()
            time = datetime.fromtimestamp(mtime)
            diff = currentTime - time
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            self.logger.info("{} Hours".format(hours))
            if(hours>=12):
                return True
            else:
                return False
        except Exception as e:
            self.logger.error("Error in Delete API "+str(e))

    def check_empty(self,path):
        directory = os.listdir(path)
        if len(directory) == 0:
            return True
        else:
            return False

    def deleteFile(self,file,path):
        try:
            os.remove(file)
        except Exception as e:
            self.logger.error("Error in Delete API "+str(e))
        if(self.check_empty(path)):
            try:
                os.rmdir(path)
            except Exception as e:
                self.logger.error("Error in Delete API "+str(e))
