################################################################################################
# views.py: Part of eventEmitter Package, Used for Checking if file is imported successfully or not 
# Classes:
# get_status_of_triggered_event
# 
################################################################################################

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import HttpRequest, Request

from django.http.response import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token
from common_files.create_response import create_failure_modified, create_success_modified, create_failure, create_success

from .models import Todolist
from .serializers import eventEmiiterSerializer

import json, requests, sched, time, sys

event = sched.scheduler(time.time, time.sleep)
  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 

sys.setrecursionlimit(10**8)
########################################################################################################
# Class get_status_of_triggered_event - Collection of functions for for tracking status of file that it is Pending,Success or Failed
# Functions:
# post - is used to take input from the client and send response to the client.
# response_filter - is used to extract only relevant response which would be sent to UI
########################################################################################################
# External Function -
# trigger_event - is used to create event is every 2 seconds and check status of file in todolist table
########################################################################################################
data = {}
def trigger_event(toDoID):
    try:
        toDoCount = Todolist.objects.filter(id=toDoID).count()
        if(toDoCount == 0):
            event.enter(2, 1, trigger_event, (toDoID,))
            event.run()
        else:
            toDo = Todolist.objects.get(id=toDoID) 
            toDoVal = list(Todolist.objects.filter(id=toDoID).values())
            if(toDo.status == 'Pending'):
                trigger_event(toDoID)
            elif(toDo.status == 'Failed'):
                data['message'] = 'fetched failed status'
                data['data'] = toDoVal
                data['status'] = 'fail'
                return json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
            else:
                data['message'] = 'fetched success status'
                data['data'] = toDoVal
                data['status'] = 'success'
                res = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
                return res
    except Exception as e:
        data['message'] = 'Error in API -'+str(e)
        data['data'] = {}
        data['status'] = 'fail'

class get_status_of_triggered_event(APIView):
    def __init__(self):
        self.logger = get_logger()

    def post(self, request):
        try:
            token = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if token == 0:
                self.logger.error("Error in Upload File Import API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail')) 
        except Exception as e:
            self.logger.error("Error in Fetching Data."+str(e))
            return JsonResponse(create_failure_modified(500, 'Data Request Error', 'Failed', '', 'failed'))
        
        try:
            toDoID = request.data['toDoID']
            try:
                toDoCount = Todolist.objects.filter(id=toDoID).count()
                if(toDoCount == 0):
                    return JsonResponse(create_failure_modified(500, 'No Entry in DB', 'Failed', '', 'failed'))
               
                else:
                    toDo = Todolist.objects.get(id=toDoID) 
                    toDoVal = list(Todolist.objects.filter(id=toDoID).values())          
                    if(toDo.status == 'Pending'):
                        trigger_event(toDoID)
                        if(data['status'] == 'success'):
                            res = self.response_filter(data['data'][0])
                            data['data'][0] = res
                            return JsonResponse(create_success(data['message'],data['data']))
                        else:
                            res = self.response_filter(data['data'][0])
                            data['data'][0] = res
                            return JsonResponse(create_failure_modified(500, data['message'],'Fail',data['data']))                            
                    elif(toDo.status == 'Failed'):
                        toDoVal[0] = self.response_filter(toDoVal[0])
                        return JsonResponse(create_failure_modified(500,'fetched failed status', 'Fail', toDoVal))
                    else:
                        toDoVal[0] = self.response_filter(toDoVal[0])
                        return JsonResponse(create_success('fetched success status', toDoVal))
                if(data['status'] == 'success'):
                    res = self.response_filter(data['data'][0])
                    data['data'][0] = res
                    return JsonResponse(create_success_modified(data['message'],data['data']))
                else:
                    res = self.response_filter(data['data'][0])
                    data['data'][0] = res                    
                    return JsonResponse(create_failure_modified(500, data['message'],'Fail', data['data']))                            
            except Exception as e:
                self.logger.error("Bad Request."+str(e))
                return JsonResponse(create_failure_modified(500, 'Bad Request', 'Fail'))
        except Exception as e:
            self.logger.error("Value Missing."+str(e))
            return JsonResponse(create_failure_modified(500, 'Value Missing', 'Fail'))

    def response_filter(self,data):
        try:
            res = {}
            res['Status'] = data['status']
            res['FailedReason'] = data['failedreason']
            res['Id'] = data['id']
        except Exception as e:
                self.logger.error("Error while filtering payload"+str(e))
        return res

