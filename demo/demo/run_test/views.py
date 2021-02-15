from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.request import HttpRequest, Request

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_connection import db_conn
from common_files.create_response import create_failure, create_success
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token

from .serializers import todolistSerializer, settingsSerializer, ruledetailsSerializer
from event_emitter.models import Todolist
from dashboard.models import Ruledetails, Settings, Testparameter, Testparameterdetail, TestClientTemplateMapping
from run_test import models
from run_test.get_sp_parameter import api_run_test, sp_runtest
from upload_file.views import FetchDatabaseName


import requests, datetime, json, zipfile, zlib, xlsxwriter, time, csv, os, uuid


# Create your views here.
class run_test_api(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.connection = db_conn()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def run_test_function(self, payload) -> JsonResponse:
        try:
            rule_id = payload['RuleID']
            session_id = payload['SessionID']
            toDoList_id = payload['ToDoListID']
            user_id = payload['UserID']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide valid key', 'Fail'))
        try:
            todayDate = datetime.datetime.now()
            testdetails = Ruledetails.objects.filter(ruleid=rule_id).values_list('ruletype','resultquery','ruledetailsid')
            if testdetails.exists():
                for testdetailsitems in testdetails:
                    try:
                        # create mapping table entry
                        sessionTestId = uuid.uuid4()
                        mappingsessiontest = models.Sessiontestmapping(sessiontestid = sessionTestId, userid = user_id, sessionid = session_id,
                                todolistid = toDoList_id, ruleid = rule_id, createddate = todayDate, ruledetailsid = testdetailsitems[2])
                        mappingsessiontest.save()
                        if str(testdetailsitems[0]) == "sp_query":
                            resSP = sp_runtest(rule_id, testdetailsitems[2])
                            if resSP['statusCode'] == 200:
                                return create_success('Success')
                            else:
                                return create_failure(500, 'Failed to execute Stored Procedure', 'Failed')
                        elif str(testdetailsitems[0]) == "api":
                            resapi = api_run_test(rule_id, testdetailsitems[2])
                            if resapi['statusCode'] == 200:
                                return create_success('Success')
                            else:
                                return create_failure(500, 'Failed to execute Stored Procedure', 'Failed')
                    except Exception as e:
                        self.logger.error("Error in parsing ruledetails table: "+str(e))
                        return create_failure(500, 'Error in parsing ruledetails table', 'Failed')
            else:
                return create_failure(500, 'No data for seleted Rule Id', 'Failed')
            self.connection.close()
        except Exception as e:
            self.logger.error("Error in fetching the tests: "+str(e))
            return create_failure(500, 'Error in parsing ruledetails table', 'Failed')
        return create_success('Success')

########################################################################################################
# Class export_test - Collection of functions for exporting test results into excel/csv file
# Functions:
# export_class - is used to create filenames and used to fetch number of sequenceids
# createFile - is used to create excel/csv file on server
########################################################################################################


class export_test():
    def __init__(self):
        self.logger = get_logger() 
        self.config = read_config()
        
    def export_class(self,ruleidVar):
        try:
            output = {}
            fileNameList = []
            ruleidValue  = ruleidVar['RuleID']
            self.logger.info(ruleidValue)
            ruleDetailsObject = Ruledetails.objects.filter(ruleid=ruleidValue)
            ruleDetailsData = ruledetailsSerializer(ruleDetailsObject, many=True)  
            if(ruleDetailsObject.exists()):
                try:
                    for ruledetailsRecord in ruleDetailsData.data:
                        try:
                            annexureFileName = ruledetailsRecord['annexurefilename']
                            if(annexureFileName != None):
                                if(ruleidVar['FileType'].lower() == 'excel'):
                                    fileName = annexureFileName + '.xlsx'
                                else:
                                    fileName = annexureFileName + '.csv'
                            else:
                                if(ruleidVar['FileType'].lower() == 'excel'):
                                    fileName = ruledetailsRecord['ruleid'] + '_' + str(ruledetailsRecord['sequenceno']) + '.xlsx'
                                else:
                                    fileName = ruledetailsRecord['ruleid'] + '_' + str(ruledetailsRecord['sequenceno']) + '.csv'
                            self.logger.info(fileName)
                            fileNameList.append(fileName)
                            dbVar = FetchDatabaseName()
                            dbName = dbVar.fetch(ruleidVar['SessionID'])
                            responseCreateFile = self.create_file(ruledetailsRecord,fileName,ruleidVar['FileType'].lower(),ruleidVar['ID'],dbName)
                            if(responseCreateFile != True):
                                return responseCreateFile
                        except Exception as e:
                            self.logger.error("Error in Export Test API during Fetching Ruleid Details from table"+str(e))
                            return create_failure(500, 'Error in Export Test API during Fetching Ruleid Details from table', 'Failed')
                except Exception as e:
                    self.logger.error("Error in Export Test API during Fetching Ruleid Details from table"+str(e))
                    return create_failure(500, 'Error in Export Test API during Fetching Ruleid Details from table', 'Failed')
            try:
                output['fileName'] = ','.join(fileNameList)
                output['appUrl'] = self.appUrl + self.config['ENV_VARIABLE']['download_files'] + ruleidVar['ID']
            except Exception as e:
                self.logger.error("Error in Export Test API during creation of output"+str(e))
                return create_failure(500, 'Error in Export Test API during creation of output', 'Failed')
        except Exception as e:
            self.logger.error("Error in Export Test API "+str(e))
            return create_failure(500, 'API Fail due to Exception', 'Failed')
        return create_success("Export API is Working",output)

    def create_file(self,ruledetailsRecord,fileName,fileType,todoId,dbName):
        try:
            settingsObject = Settings.objects.all()
            settingsData = settingsSerializer(settingsObject, many=True) 
            if(settingsData.data):
                try:
                    filePath = settingsData.data[0]['outputrootdirectory']
                    self.appUrl = settingsData.data[0]['appurl']
                except Exception as e:
                    self.logger.error("Error in Settings Table "+str(e))
                    return create_failure(500, 'Error in Settings Table', 'Failed')
            else:
                self.logger.error("Error in Settings Table "+str(e))
                return create_failure(500, 'Error in Settings Table', 'Failed')

            try:    
                self.connection = db_conn(dbName)
                cursor = self.connection.cursor()
            except Exception as e:
                self.logger.error("Error while Creating Database Connection: "+str(e))
                return create_failure(500, 'Error while Creating Database Connection', 'Failed')

            directory = filePath + '/' + todoId
            if not os.path.exists(directory):
                os.makedirs(directory)

            try:
                resultset = cursor.execute(ruledetailsRecord['resultquery']).fetchall()
                fieldName = [field[0] for field in cursor.description]
                cursor.close()
                self.connection.close()
                dateColumns = []
                dateFlag = False
                # For finding date time object
                for i in range(len(resultset[0])):
                    try:
                        if(type(resultset[0][i]) == datetime.datetime):
                            dateColumns.append(i)
                            dateFlag = True
                    except Exception as e:
                        self.logger.error("Error while Handling DateObjects "+str(e))
                        return create_failure(500, 'Error while Handling DateObjects', 'Failed')
            except Exception as e:
                self.logger.error("Error while Fetching Table Data: "+str(e))
                return create_failure(500, 'Error while Fetching Table Data', 'Failed')
                

            if(fileType == 'excel'):
                with xlsxwriter.Workbook(directory+ '/' + fileName) as workbook:
                    try:                                                
                        worksheet = workbook.add_worksheet()
                        for colNum, data in enumerate(fieldName):
                            try:
                                worksheet.write(0, colNum, data)
                            except Exception as e:
                                self.logger.error("Error while writing in Excel File "+str(e))
                                return create_failure(500, 'Error while writing in Excel File', 'Failed')
                        for rowNum, data in enumerate(resultset):
                            try:
                                if(dateFlag == True):
                                    for i in dateColumns:
                                        data[i] = str(data[i])
                                worksheet.write_row(rowNum+1, 0, data)
                            except Exception as e:
                                self.logger.error("Error while writing in Excel File "+str(e))
                                return create_failure(500, 'Error while writing in Excel File', 'Failed')
                    except Exception as e:
                        self.logger.error("Error while writing in Excel File "+str(e))
                        return create_failure(500, 'Error while writing in Excel File', 'Failed')
            else:
                with open(directory+ '/' + fileName, 'w', newline='') as file:
                    try:
                        csvWriter = csv.writer(file)
                        csvWriter.writerow(fieldName)
                        for rowNum, data in enumerate(resultset):
                            if(dateFlag == True):
                                for i in dateColumns:
                                    data[i] = str(data[i])
                            csvWriter.writerow(data)
                    except Exception as e:
                        self.logger.error("Error while writing in CSV File "+str(e))
                        return create_failure(500, 'Error while writing in CSV File', 'Failed')
        except Exception as e:
            self.logger.error("Error in fetching the tests: "+str(e))
            return create_failure(500, 'Error in fetching the tests', 'Fail')
        return True

########################################################################################################
# Class download_zip - Collection of functions for zipping excel/csv Files
# Functions:
# post - is used to zip files and return zip file path
########################################################################################################

class download_zip(APIView):
    def __init__(self):
        self.logger = get_logger() 
        self.config = read_config()
    def post(self,request : Request) -> JsonResponse:
        try:
            token = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if token == 0:
                self.logger.error("Error in Download API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Failed'))
        except Exception as e:
            self.logger.error("Error in Download API."+str(e))
            return JsonResponse(create_failure(500, 'Authentication Error', 'Failed'))

        try:
            toDoListID = request.data['toDoListID']
            zipFilePath = self.config['ENV_VARIABLE']['file_path_zip']
            downloadFilePath = self.config['ENV_VARIABLE']['file_path_download']
            if not os.path.exists(zipFilePath):
                os.makedirs(zipFilePath)
            try:
                settingsObject = Settings.objects.all()
                settingsData = settingsSerializer(settingsObject, many=True) 
                if(settingsData.data):
                    try:
                        appUrl = settingsData.data[0]['appurl']
                        self.zipCount = settingsData.data[0]['layercount']
                    except Exception as e:
                        self.logger.error("Failed to convert files into zip "+str(e))
                        return JsonResponse(create_failure(500, 'Failed to convert files into zip - Error in Settings Table', 'Failed'))
                else:
                    self.logger.error("Failed to convert files into zip - Error in Settings Table "+str(e))
                    return JsonResponse(create_failure(500, 'Failed to convert files into zip - Error in Settings Table', 'Failed'))
            except Exception as e:
                self.logger.error("Failed to convert files into zip "+str(e))
                return JsonResponse(create_failure(500, 'Failed to convert files into zip - Error in Settings Table', 'Failed'))
            urlList = []
            filePathList = []
            for toDoID in toDoListID:
                try:
                    toDoListObject = Todolist.objects.filter(id=toDoID)
                    todoListData = todolistSerializer(toDoListObject, many=True) 
                    if(todoListData.data):
                        try:
                            fileName = todoListData.data[0]['outputfilename']
                            fileList = fileName.split(',')
                            for files in fileList:
                                urlJson = dict()
                                url = appUrl + self.config['ENV_VARIABLE']['download_files'] + toDoID + '/' + files
                                urlJson['ID'] = toDoID 
                                urlJson['DownloadUrl'] = url
                                urlJson['Zip'] = False
                                urlList.append(urlJson)
                                filePath = toDoID + '/' + files
                                filePathList.append(filePath)
                        except Exception as e:
                            self.logger.error("Failed to Fetch Output file name - Error in Todolist Table "+str(e))
                            return JsonResponse(create_failure(500, 'Failed to Fetch Output file name - Error in Todolist Table ', 'Failed'))                       
                except Exception as e:
                    self.logger.error("Failed to Fetch Output file name - Error in Todolist Table "+str(e))
                    return JsonResponse(create_failure(500, 'Failed to Fetch Output file name - Error in Todolist Table ', 'Failed'))                         
            if(len(filePathList) >= self.zipCount):
                compression = zipfile.ZIP_DEFLATED
                now = datetime.datetime.now()
                timeStamp = datetime.datetime.timestamp(now)
                zipfileName = zipFilePath + str(timeStamp) + ".zip"
                zipFiles = zipfile.ZipFile(zipfileName, mode="w")
                for files in filePathList:
                    try:
                        fileName = files.split("/")[-1]
                        filesVar = downloadFilePath + files
                        zipFiles.write(filesVar, fileName, compress_type=compression)
                    except Exception as e:
                        self.logger.error("Failed to convert files into zip"+str(e))
                        return JsonResponse(create_failure(500, 'Failed to convert files into zip', 'Failed'))
                zipFiles.close()
                zipUrl = appUrl + self.config['ENV_VARIABLE']['zip_files'] + str(timeStamp) + '.zip'
                for i in range(len(urlList)):
                    urlList[i]['DownloadUrl'] = zipUrl
                    urlList[i]['Zip'] = True
            output = {'DownloadURL' : urlList}
        except Exception as e:
            self.logger.error("Failed to convert files into zip "+str(e))
            return JsonResponse(create_failure(500, 'Failed to convert files into zip', 'Failed'))
        return JsonResponse(create_success('URL Generated Successfully',output ))

 

class powerbi_url(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})
    
    def powerbi(self, payload) -> JsonResponse:
        try:
            ruleid = payload['ruleid']
            ruleid_url = TestClientTemplateMapping.objects.filter(ruleid=ruleid).values_list('url')
            try:
                url = ruleid_url[0][0]
            except Exception as e:
                self.logger.error("No URL found for selected ruleid: "+str(e))
                return create_failure(500, 'No URL found for selected ruleid', 'Failed')
        except Exception as e:
            self.logger.error("Error in Powerbi url: "+str(e))
            return create_failure(500, 'Error in Powerbi url', 'Failed')
        return create_success('Success')

