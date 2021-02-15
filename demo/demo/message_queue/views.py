################################################################################################
# views.py: Part of messageQueue Package, Used for Publish Message Functionality
# Classes:
# publish_message
#
# Change Log:
# Class publish_message - 
# 11/07/2020 - Initial Creation
#
# 23/07/2020 - Integration of Publish Message With UploadScheduler and UploadFileDump
################################################################################################

from django.http.response import JsonResponse
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.request import HttpRequest,Request

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token
from common_files.create_response import create_failure, create_success

from event_emitter.models import Todolist

from upload_file.dump_file import dump_file
from upload_file.views import FetchDatabaseName
from run_test.views import run_test_api, export_test, powerbi_url
from new_session.views import new_session

from django.core.mail import send_mail, EmailMessage
import datetime

import json,requests,pika,json,base64,pytz,time
import hashlib

########################################################################################################
# Class publish_message - Collection of functions for importing files
# Functions:
# post - is used to take input from the client and send response to the client.
# insert_todo_list - is used to insert entry of File(excel,csv) based on todoid and set it entry to Pending.
# update_todo_list - is used to update status of File that is successfully dumped into the DB or not.
########################################################################################################
class publish_message(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.config = read_config()

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in Publish Message API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in Publish Message API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            #for send email!
            sendMailFlag = False
            attachFilepath = []
            
            # To insert record into ToDoList table
            for requestDataVar in request.data:
                try:
                    statusInsert = self.insert_todo_list(requestDataVar)
                    # for Run-Test API
                    if(self.eventType == 'TestExec'):
                        try:
                            # TODO: implement messageQueue and scheduler
                            payload = {"RuleID": requestDataVar['RuleID'],
                                        "SessionID": requestDataVar['SessionID'],
                                        "ToDoListID":requestDataVar['ID'],
                                        "UserID":userid}
                            runTest = run_test_api()
                            responseRuntest = runTest.run_test_function(payload)
                            if responseRuntest['statusCode'] == 200:
                                self.update_todo_list(request,"Success")
                            else:
                                self.update_todo_list(request, responseRuntest['replyCode'], responseRuntest['message'])
                        except Exception as e:
                            self.logger.error("Error in run test execution API: "+str(e))
                            self.update_todo_list(request, "Failed", str(e))

                    # For Upload file functionality
                    elif(self.eventType == 'Import'):
                        try:
                            dbVar = FetchDatabaseName()
                            dbName = dbVar.fetch(self.sessionId)
                            if(len(dbName)!=0):
                                try:
                                    if(self.fileType == 'CSV'):
                                        payload = {"FileType" : self.fileType,"ClientID": self.clientId,"FilePath": self.filePath,"SheetName": self.sheetName,
                                            "Overwrite_merge":self.overWriteMerge,"DatabaseName":dbName,"TableName":self.tableName,
                                            "textqualifier":self.textQualifier,"rowdelimeter":self.rowDelimeter,"columndelimeter":self.columnDelimeter,
                                            "numberRowToSkip":self.numberRowToSkip,"iscolumnnameinfirstrow":self.isColumnNameInFirstRow}
                                    else:
                                        payload = {"FileType" : self.fileType,"ClientID": self.clientId,"FilePath": self.filePath,"SheetName": self.sheetName,
                                            "Overwrite_merge":self.overWriteMerge,"DatabaseName":dbName,"TableName":self.tableName}
                                    resUpload = dump_file(payload)
                                    if(resUpload['statusCode'] == 200):
                                        self.update_todo_list(request,"Success")    
                                    else:
                                        self.logger.info("Response DumpFile- {}".format(resUpload))
                                        self.update_todo_list(request,"Failed",resUpload['message'])    
                                except Exception as e:
                                    self.logger.error("Error in DumpFile: "+str(e))
                                    self.update_todo_list(request,"Failed",str(e))                            
                            else:
                                self.logger.info("Response FetchDB- {}".format(dbName))
                                self.update_todo_list(request,"Failed",dbName['message'])
                        except Exception as e:
                            self.logger.error("Error in FetchDB: "+str(e))
                            self.update_todo_list(request,"Failed",str(e))

                    # For Export test output file    
                    elif(self.eventType == 'Output'):
                        try:
                            classVar = export_test()
                            resExport = classVar.export_class(requestDataVar)
                            if(resExport['statusCode'] == 200):
                                self.fileName = resExport['data']['fileName']
                                self.appUrl = resExport['data']['appUrl']
                                self.update_todo_list(request,"Success",'Output')    
                            else:
                                self.logger.error("Response Export- {}".format(resExport))
                                self.update_todo_list(request,"Failed",resExport['message'])    
                        except Exception as e:
                            self.logger.error("Error in Export Test: "+str(e))
                            self.update_todo_list(request,"Failed",str(e))
                    
                    # for sending Email
                    elif(self.eventType == 'Email'):
                        try:
                            classVar = export_test()             #using export function to attaching files in Email                
                            resExport = classVar.export_class(requestDataVar)
                            if(resExport['statusCode'] == 200):
                                self.fileName = resExport['data']['fileName']
                                self.outputPublishFolderPath = self.config['ENV_VARIABLE']['file_path_download'] + requestDataVar['ID']
                                self.appUrl = resExport['data']['appUrl']
                                self.update_todo_list(request,"Success",'Output')
                                attachFilepath.append(str(self.outputPublishFolderPath) +"/"+str(self.fileName))
                                print(attachFilepath)
                                try:
                                    emailIds = requestDataVar['To']                     # stroing email from request pyaload     
                                    emailIds = emailIds.split(';')                      # spliting emails from string to List
                                    emailIds = [x.strip(' ') for x in emailIds]         # storing email ids  without white spaces
                                    sendMailFlag = True                                 # to confirm for sending email
                                except Exception as e:
                                    self.logger.error("Error In Fething Emails",str(e))
                            else:
                                self.logger.error("Response Export- {}".format(resExport))
                                self.update_todo_list(request,"Failed",resExport['message'])    
                        except Exception as e:
                            self.logger.error("Error in Export Test for sending email: "+str(e))
                            self.update_todo_list(request,"Failed",str(e)) 

                    # For creating New Session
                    elif(self.eventType == 'NewSession'):
                        try:
                            #TODO: Implement scheduler and messageQueue
                            payload = {"ClientID":requestDataVar['ClientID'],
                                        "SessionID":requestDataVar['SessionID'],
                                        "AuditFrom":requestDataVar['AuditFrom'],
                                        "AuditTo":requestDataVar['AuditTo'],
                                        "ProjectName":requestDataVar['ProjectName'],
                                        "SerialNo":requestDataVar['SerialNo'],
                                        "userid":userid}
                            newSess = new_session()
                            responseNewSess = newSess.post(payload)
                            if responseNewSess['statusCode'] == 200:
                                self.update_todo_list(request,"Success")
                            else:
                                self.update_todo_list(request, responseNewSess['replyCode'], responseNewSess['message'])
                        except Exception as e:
                            self.logger.error("Error in new session API: "+str(e))
                            self.update_todo_list(request,"Failed",str(e)) 

                    # For Power BI URL Validity
                    elif(self.eventType == 'ViewInPowerBI'):
                        try:
                            payload = {"ruleid":requestDataVar['RuleID']}
                            powerbi_func = powerbi_url()
                            response_powerbi = powerbi_func.powerbi(payload)
                            if response_powerbi['statusCode'] == 200:
                                self.update_todo_list(request,"Success")
                            else:
                                self.update_todo_list(request, response_powerbi['replyCode'], response_powerbi['message'])
                        except Exception as e:
                            self.logger.error("Error in powerbi url API: "+str(e))
                            self.update_todo_list(request, "Failed", str(e))
                except Exception as e:
                    self.logger.error("Error in Publish Message API: "+str(e))
                    return JsonResponse(create_failure(400, 'Error in Publish Message API', 'Fail'))

            if sendMailFlag: #if true mail will be send
                self.send_email(attachFilepath,emailIds) #calling send_email Function
        except Exception as e:
            self.logger.error("Error in publish_message API: "+str(e))
            return JsonResponse(create_failure(500, 'Error in publish_message API', 'Fail'))
        return JsonResponse(create_success('Success', ''))

    def insert_todo_list(self,requestDataVar):
        status = "Pending"
        try:
            self.clientId = requestDataVar['ClientID']
        except:
            self.clientId = None
        try:
            self.eventType = requestDataVar['EventType'] 
        except:
            self.eventType = None  
        try:
            self.filePath = requestDataVar['FilePath'] 
        except:
            self.filePath = None 
        try:
            self.fileType = requestDataVar['FileType'] 
        except:
            self.fileType = None
        try:
            self.todoId = requestDataVar['ID'] 
            self.logger.info("TO-Do ID - {}".format(self.todoId))
        except:
            self.todoId = None
        try:
            self.sessionId = requestDataVar['SessionID']
        except: 
            self.sessionId = None
        try:
            self.sheetName = requestDataVar['Sheet_Name']
        except:
            self.sheetName = None
        try:
            self.tableName = requestDataVar['TableName']
        except:
            self.tableName = None
        try:
            self.textQualifier = requestDataVar['textqualifier'] 
        except:
            self.textQualifier = "NULL"
        try:
            self.rowDelimeter = requestDataVar['rowdelimeter']
            decodeRow = base64.b64decode(self.rowDelimeter).decode("utf-8")
        except:
            self.rowDelimeter = None
            decodeRow = None
        try:
            self.columnDelimeter = requestDataVar['columndelimeter']
            decodeColumn = base64.b64decode(self.columnDelimeter).decode("utf-8") 
        except:
            self.columnDelimeter = None 
            decodeColumn = None
        try:
            self.numberRowToSkip = requestDataVar['numberRowToSkip']
        except:
            self.numberRowToSkip = None
        try:
            self.isColumnNameInFirstRow = requestDataVar['iscolumnnameinfirstrow'] 
        except:
            self.isColumnNameInFirstRow = None
        try:
            self.overWriteMerge = requestDataVar['Overwrite_Merge'] 
        except:
            self.overWriteMerge = None
        try:
            self.ruleId = requestDataVar['RuleID'] 
        except:
            self.ruleId = None
        try:
            currentTime = timezone.now()
            todoRecord = Todolist(clientid=self.clientId,status=status,createdon=currentTime,eventtype=self.eventType,
                filepath=self.filePath,filetype=self.fileType,id=self.todoId,sessionid=self.sessionId,sheet_name=self.sheetName,
                tablename=self.tableName,text_qualifier=self.textQualifier,row_delimiter=decodeRow,
                column_delimiter=decodeColumn,header_row_delimiter=self.isColumnNameInFirstRow,header_rows_to_skip=self.numberRowToSkip,
                overwrite_merge = self.overWriteMerge, ruleid=self.ruleId)
            todoRecord.save()
            return True
        except Exception as e:
            self.logger.error("Error while inserting into DB: "+str(e))
            return False
    
    def update_todo_list(self,request,status,failedReason=None):
        try:
            if(self.eventType == 'Output' and status == 'Success'):
                response = Todolist.objects.filter(id=self.todoId).update(status=status, outputfilename = self.fileName, outputfolderpath = self.appUrl)
            else:
                response = Todolist.objects.filter(id=self.todoId).update(status=status,failedreason=failedReason)
        except Exception as e:
            self.logger.error("Error while inserting into DB: "+str(e))

    def send_email(self,attachFilepath,toSend):
        self.config = read_config()
        output = {
        'statusCode' : '200',
        'message' : 'Email Sent.',
        'replyCode' : 'Success'
        }
        try:
            if len(toSend) == 0:
                output['statusCode'] = '400'
                output['message'] = 'Please Provide Email Id'
                output['replyCode'] = 'Failed'
            fromEmail = self.config['SEND_EMAIL']['from']
            subject = self.config['SEND_EMAIL']['subject']
            message = self.config['SEND_EMAIL']['message']
            mail = EmailMessage(subject, message, fromEmail, toSend)
            try:
                for files in attachFilepath :
                    try:
                        mail.attach_file(str(files))
                    except Exception as e :
                        self.logger.error("Error while attaching files"+str(e))
            except Exception as e:
                self.logger.error("Error while attaching files"+str(e))
            try:
                mail.send()
            except Exception as e:
                print("Cant Send"+str(e)+"")
        except Exception as e:
            output['statusCode'] = '400'
            output['message'] = 'Email Cannot Sent'
            output['replyCode'] = 'Failed'
            self.logger.error("Error while Sending Email"+str(e))
        return output
