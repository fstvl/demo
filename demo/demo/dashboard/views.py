from django.http.response import JsonResponse
from django.apps import apps
from rest_framework.views import APIView
from rest_framework.request import HttpRequest, Request

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_connection import db_conn
from common_files.create_response import create_failure, create_success
from sql_queries.dashboard_sql_query import get_table_data_for_date_range_sql, get_fetch_table_details, get_sql_query_fetch_tests
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token

from dashboard import models
from .models import Settings, Sectormaster, Usertosectormapping, Usertoclientmapping, Clientmaster, Riskcontrol, Riskdetail, Riskmaster
from event_emitter.models import Todolist
from .serializers import settingSerializer, sectormasterSerializer, usertosectormappingSerializer, testparameterSerializer, TestparameterdetailSerializer, ExcelimportmappingmainSerializer, RiskControlSerializer, RiskDetailSerializer, RiskMasterSerializer

from django.db.models import Q
import json, requests, datetime, uuid


# Create your views here.
class get_labels(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getlables API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getlables API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            usersettingamapp = models.Usertosettingsmapping.objects.filter(userid=userid).values_list("settingsid")
            if usersettingamapp.exists():
                settingsid = usersettingamapp[0][0]
                settingsdata = models.Settings.objects.filter(settingsid=settingsid)
                labels_data = settingSerializer(settingsdata, many=True)
                if not labels_data.data:
                    return JsonResponse(create_failure(500, 'Error in fetching the data', 'Fail'))
                else:
                    output = create_success('fetched labels for start page tab.', labels_data.data)
            else:
                self.logger.error("Error in getlables API: No mappings found ")
                return JsonResponse(create_failure(400, 'getLabels API Fail', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getlables API: "+str(e))
            return JsonResponse(create_failure(400, 'getLabels API Fail', 'Fail'))
        return JsonResponse(output)


class get_sector_for_selected_user_id_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getSectorForSelectedUserID API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getSectorForSelectedUserID API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            UsertosectormappingList = Usertosectormapping.objects.filter(userid=userid).values_list('sectorid', flat=True)
            try:
                resultlist = []
                for elem in UsertosectormappingList:
                    sectordataqueryset = Sectormaster.objects.filter(sectormasterid=elem).values_list('testresultprefix','sector', 'sectormasterid', 'lefticonlablecaption')
                    if sectordataqueryset.exists():
                        sectordataDict = {}
                        for item in sectordataqueryset:                    
                            sectordataDict['TestResultPrefix'] = item[0]
                            sectordataDict['Sector'] = item[1]
                            sectordataDict['ID'] = item[2]
                            sectordataDict['LeftIconLableCaption'] = item[3]
                        resultlist.append(sectordataDict)
                output = create_success('fetched sector for selected user id.', resultlist)
            except Exception as e:
                self.logger.error("error in fetching data from models: " +str(e))
                return JsonResponse(create_failure(500, 'invalid user id', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getSectorForSelectedUserIDAPI : "+str(e))
            return JsonResponse(create_failure(500, 'Bad Request', 'Fail'))
        return JsonResponse(output)


class get_client_for_selected_user_id_and_sector_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getClientForSelectedUserIDAndSector API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getClientForSelectedUserIDAndSector API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            sector_id = request.data['sector_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide sector_id', 'Fail'))
        try:
            try:
                userclientmappingobj = Usertoclientmapping.objects.filter(userid=userid).values_list('clientid', flat=True)
                clientmasterdatalist = []
                for userclientid in userclientmappingobj:
                    clientmasterdata = Clientmaster.objects.filter(clientmasterid=userclientid, isactive=1, 
                        sector=sector_id).values_list('clientname','sessionid','clientmasterid','iftestsarebyrisk','allowcreatenewsession')
                    if clientmasterdata.exists():
                        clientmasterdict = {}
                        for item in clientmasterdata:
                            clientmasterdict['ClientName'] = item[0]
                            clientmasterdict['SessionID'] = item[1]
                            clientmasterdict['ID'] = item[2]
                            clientmasterdict['IfTestsAreByRisk'] = item[3]
                            clientmasterdict['AllowCreateNewSession'] = item[4]
                        clientmasterdatalist.append(clientmasterdict)
                output = create_success('fetched client for selected sector id.', clientmasterdatalist)
            except Exception as e:
                self.logger.error("Error in getClientForSelectedUserIDAndSectorAPI : "+str(e))
                return JsonResponse(create_failure(500, 'invalid user id or sector id', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getClientForSelectedUserIDAndSectorAPI : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


class get_process_for_selected_client_id_and_sector_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getProcessForSelectedClientIDAndSector API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getProcessForSelectedClientIDAndSector API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            sector_id = request.data['sector_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide sector_id', 'Fail'))
        try:
            client_id = request.data['client_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide client_id', 'Fail'))
        try:
            resultlist = []
            try:
                clientProcessMapping = models.Clienttoprocessmapping.objects.filter(clientid=client_id).values_list('processid', flat=True)
                for clientProcessMappingid in clientProcessMapping:
                    processmasterdata = models.Processmaster.objects.filter(pid='-1',processmasterid=clientProcessMappingid, 
                        sector=sector_id).values_list('processmasterid','processname','processdescription')
                    if processmasterdata.exists():
                        processmasterdict = {}
                        for items in processmasterdata:
                            processmasterdict['ID']=items[0]
                            processmasterdict['ProcessName']=items[1]
                            processmasterdict['ProcessDescription']=items[2]
                        resultlist.append(processmasterdict)
                output = create_success('fetched process for selected sector and client id.',resultlist)
            except Exception as e:
                self.logger.error("Error in fetching data from db : "+str(e))
                return JsonResponse(create_failure(500, 'invalid client id or sector id.', 'Fail'))
        except Exception as e:
            self.logger.error("Error in get process for selected client id and sector id : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


class get_current_database_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getlables API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getlables API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            client_id = request.data['client_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide client_id', 'Fail'))
        try:
            databasesettingtable = models.TblMDatabasesettings.objects.all().values_list('databasesettingsid',
                'databasename','servername','username','password','iswinauthentication')
            currentdatabaselist = []
            if databasesettingtable.exists():
                for databasesettingitems in databasesettingtable:
                    try:
                        sessionmaintable = models.Sessionmain.objects.filter(dbid=databasesettingitems[0]).values_list('sessionmainid','dbid')
                        if sessionmaintable.exists():
                            for sessionmainid in sessionmaintable:
                                clientmasterdata = models.Clientmaster.objects.filter(clientmasterid=client_id, isactive='1', 
                                    sessionid=sessionmainid[0]).values_list('clientmasterid', 'sessionid')
                                if clientmasterdata.exists():
                                    databaseitemdict = {}
                                    for items in clientmasterdata:
                                        databaseitemdict['ClientID'] = items[0]
                                        databaseitemdict['ID'] = sessionmainid[0]
                                        databaseitemdict['DatabaseName'] = databasesettingitems[1]
                                        databaseitemdict['ServerName'] = databasesettingitems[2]
                                    currentdatabaselist.append(databaseitemdict)
                    except Exception as e:
                        self.logger.error("Error in fetching data from db : "+str(e))
                        return JsonResponse(create_failure(500, 'invalid client id', 'Fail'))
            output = create_success('fetched current database',currentdatabaselist)
        except Exception as e:
            self.logger.error("Error in getcurrent database : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


class get_subprocess_for_selected_client_id_and_process_id_api(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getlables API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getlables API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            client_id = request.data['client_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide client_id', 'Fail'))
        try:
            process_id = request.data['process_id']
        except Exception as e:
            self.logger.error("Error in fetching data from db : "+str(e))
            return JsonResponse(create_failure(500, 'Please provide process_id', 'Fail'))
        try:
            resultset = []
            clientsubprocessmapp = models.Clienttosubprocessmapping.objects.filter(clientid=client_id).values_list('subprocessid', flat=True)
            
            for clientsubprocessid in clientsubprocessmapp:
                try:
                    processmasterdata = models.Processmaster.objects.filter(processmasterid=clientsubprocessid, pid=process_id).values_list('pid',
                        'processmasterid','testno','subprocessname','subtitle','processdescription')
                    subprocessdict = {}
                    for pmdata in processmasterdata:
                        rulemastercount = models.Rulemaster.objects.filter(~Q(pid='-1'), processid=pmdata[1]).count()
                        subprocessdict['TestCount'] = rulemastercount
                        subprocessdict['ID'] = pmdata[1]
                        subprocessdict['PID'] = pmdata[0]
                        subprocessdict['TestNo'] = pmdata[2]
                        subprocessdict['Caption'] = pmdata[3]
                        subprocessdict['SubTitle'] = pmdata[4]
                        subprocessdict['ProcessDescription'] = pmdata[5]
                    if len(subprocessdict) > 0 :
                        resultset.append(subprocessdict)
                except Exception as e:
                    self.logger.error("Error in fetching data from db : "+str(e))
                    return JsonResponse(create_failure(500, 'invalid client id and process id.', 'Fail'))
            if len(resultset) > 0 : 
                output = create_success('fetched sub-process for selected client id and process id.', resultset)
            else:
                output = create_success('No Content', [])
        except Exception as e:
            self.logger.error("Occured error while fetching process of selected client id and process id:"+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


# using Stored Procedure for this API
class get_table_data_for_selected_sub_process_id(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.connection = db_conn()
    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})
    def post(self, request: Request) -> JsonResponse:
        try:
            try:
                userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
                if userid == 0:
                    self.logger.error("Error in getlables API token: ")
                    return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
            except Exception as e:
                self.logger.error("Error in getlables API: "+str(e))
                return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
            try:
                databaseName = request.data['database_name']
            except Exception as e:
                self.logger.error("invalid database name : "+str(e))
                return JsonResponse(create_failure(400, 'please provide database_name key', 'Fail'))
            try:
                subprocessId = tuple(request.data['subprocess_id'])
            except Exception as e:
                self.logger.error("invalid database or subprocess id : "+str(e))
                return JsonResponse(create_failure(400, 'please provide subprocess_id key', 'Fail'))
            try:
                riskId = tuple(request.data['risk_id'])
            except Exception as e:
                self.logger.error("invalid database or risk id : "+str(e))
                return JsonResponse(create_failure(400, 'please provide risk_id key', 'Fail'))
            try:
                ruleId = tuple(request.data['rule_id'])
            except Exception as e:
                self.logger.error("invalid database or rule id : "+str(e))
                return JsonResponse(create_failure(400, 'please provide rule_id key', 'Fail'))

            try:
                resultSet = []
                cursor = self.connection.cursor()
                query = get_fetch_table_details(databaseName,riskId,subprocessId,ruleId)
                queryResult = cursor.execute(query).fetchall()
                # Getting column names
                columnDescription=cursor.execute(query).description 
                columnName = []
                for column in columnDescription:
                    try:
                        columnName.append(column[0])
                    except Exception as e:
                        self.logger("Exception in subprocess id: ",str(e))
                        return JsonResponse(create_failure(500, 'invalid query', 'Fail'))
            except Exception as e:
                self.logger.error("error in db connection : "+str(e))
                return JsonResponse(create_failure(400, 'invalid query', 'Fail'))
            if not queryResult:
                return JsonResponse(create_success('No Content', []))
            else:
                try:
                    queryData = []
                    for rowData in queryResult:
                        queryObject = {}
                        for (value,column) in zip(rowData,columnName):
                            queryObject[column]=value
                        queryData.append(queryObject)
                    tableData = {}
                    for val in queryData:
                        if val['TableCaption'] not in tableData.keys():
                            tableData[val['TableCaption']] = {
                                'TableCaption' : val['TableCaption'],
                                'TableName' : val['TableName'],  
                                'AutomatedManual' : val['AutomatedManual'],    
                                'HasDateRangeFilter' : val['HasDateRangeFilter'],                                 
                                'DefaultColumnOnDateRangeFilter' : val['DefaultColumnOnDateRangeFilter'],                                
                                'ModifiedDate' : val['ModifiedDate'],
                                'UploadStatus' : val['UploadStatus'],
                                'FileType' : val['FileType'], 
                                'Counts' : val['Counts'], 
                                'CountsCopy' : val['Counts'], 
                                'Schema' : [],
                                'SourceSystem':databaseName}
                        else:
                            tableData[val['TableCaption']]['Schema'].append({
                                'ColumnName' : val['ColumnName'], 
                                'DataType' : val['DataType'], 
                                'Length' : val['CharacterMaximumLength'], 
                                'IsRequired' : val['IsRequired'],}) 
                    for key,val in tableData.items():
                        resultSet.append(val)
                except Exception as e:
                    self.logger.error("error in db connection : "+str(e))
                    return JsonResponse(create_success('No Content', []))
                output = create_success('fetched table data with schema of respective table name for selected sub-process id', resultSet)
            self.connection.close()
        except Exception as e:
            self.logger.error("Occured error while fetching table data with schema of respective table name of selected sub-process id : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


class get_list_of_session_id(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in listof session id API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in listofsessionId API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            clientId = request.data['client_id']
        except Exception as e:
            self.logger.error("invalid : clientId "+str(e))
            return JsonResponse(create_failure(500, 'Please provide client_id', 'Fail'))
        try:
            datalist = []
            try:
                databasesettingdata = models.TblMDatabasesettings.objects.all().values_list('databasesettingsid','servername',
                    'databasename','username','password','iswinauthentication')
                for databasesettingitems in databasesettingdata:
                    sessionmaindata = models.Sessionmain.objects.filter(dbid=databasesettingitems[0], clientid=clientId, userid=userid).values_list('sessionmainid',
                        'clientid','serialno','projectname','auditfrom','auditto','dbid')
                    if sessionmaindata.exists():
                        for sessionmainitems in sessionmaindata:
                            clintMasterdata = models.Clientmaster.objects.filter(clientmasterid=sessionmainitems[1]).values_list('clientname',
                                'sessionid','isactive')
                            if clintMasterdata.exists():
                                sessioniddict = {}
                                for clientmasteritems in clintMasterdata:
                                    sessioniddict['ClientName'] = clientmasteritems[0]
                                    sessioniddict['SessionID'] = clientmasteritems[1]
                                    sessioniddict['IsActive'] = clientmasteritems[2]
                                    sessioniddict['ID'] = sessionmainitems[0]
                                    sessioniddict['SerialNo'] = sessionmainitems[2]
                                    sessioniddict['ProjectName'] = sessionmainitems[3]
                                    if sessionmainitems[4] is not None:
                                        sessioniddict['AuditFrom'] = str((sessionmainitems[4]).date())
                                    else:
                                        sessioniddict['AuditFrom'] = sessionmainitems[4]
                                    if sessionmainitems[4] is not None:
                                        sessioniddict['AuditTo'] = str((sessionmainitems[5]).date())
                                    else:
                                        sessioniddict['AuditTo'] = sessionmainitems[5]
                                    sessioniddict['ServerName'] = databasesettingitems[1]
                                    sessioniddict['DatabaseName'] = databasesettingitems[2]
                            datalist.append(sessioniddict)
                output = create_success('fetched list of session ID for selected client id',datalist)
            except Exception as e:
                self.logger.error("Error in db connection"+str(e))
                return JsonResponse(create_failure(500, 'invalid client id', 'Fail'))
        except Exception as e:
            self.logger.error("Occured error while fetching list of session ids for selected client id : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)


# Using Stored Procedure for fetchimg the data
class get_select_test_for_selected_subprocess_id(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.connection = db_conn()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getSelectTestForSelectedSubprocessID API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getSelectTestForSelectedSubprocessID API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            databaseName = request.data['database_name']
            riskId = tuple(request.data['risk_id'])
        except Exception as e:
            self.logger.error("invalid database name or risk id"+str(e))
            return JsonResponse(create_failure(400, 'invalid database name or risk id', 'Fail'))
        try:
            cursor = self.connection.cursor()
            query = get_sql_query_fetch_tests(databaseName,riskId)
            try:
                queryResult = cursor.execute(query).fetchall()
            except Exception as e:
                self.logger.error("Error in db connection"+str(e))
                return JsonResponse(create_failure(500, 'invalid subprocess id.', 'Fail'))
            try:
                columnDescription = cursor.execute(query).description
                columnName = []
                for column in columnDescription:
                    columnName.append(column[0])
            except Exception as e:
                self.logger.error("Error in db connection"+str(e))
                return JsonResponse(create_failure(500, 'invalid subprocess id.', 'Fail'))
            try:
                resultSet = []
                for row in queryResult:
                    tableData = {}
                    for (val,column) in zip(row,columnName):
                            tableData[column]=val
                    resultSet.append(tableData)
                output = create_success('fetched test for selected sub process id',resultSet)
            except Exception as e:
                self.logger.error("Error in fething table data"+str(e))
                return JsonResponse(create_failure(500, 'invalid subprocess id.', 'Fail'))
            self.connection.close()
        except Exception as e:
            self.logger.error("Occured error while fetching test for selected sub process id : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)        


class get_test_parameter_for_selected_rule_id(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getTestParameterForSelectedRuleID API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getTestParameterForSelectedRuleID API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            rule_id = request.data['rule_id']
        except Exception as e:
            self.logger.error("invalid rule id"+str(e))
            return JsonResponse(create_failure(500, 'provide rule_id', 'Fail'))
        try:
            resultList = []
            try:
                for ruleid in rule_id:
                    ruledetailsid = models.Ruledetails.objects.filter(ruleid=ruleid).values_list('ruledetailsid', flat=True)
                    for ruleiddetails in ruledetailsid:
                        testparameteridlist = models.Testparameter.objects.filter(ruledetailsid=ruleiddetails).values_list('testparameterid')
                        parameterlist = []
                        for parameterids in testparameteridlist:
                            parameterlist.append(parameterids[0])
                        for testparameterid in parameterlist:
                            datadict = {}
                            testparamdetails = models.Testparameterdetail.objects.filter(parameterid=testparameterid).order_by('-createddate').values_list('parameterid',
                                'createddate','value','sessionid','sessiondetailid','testparameterdetailid','modifieddate')[0]
                            tmdata = models.Testparameter.objects.filter(ruledetailsid=ruleiddetails, testparameterid=testparameterid)
                            TMserialize_data = testparameterSerializer(tmdata, many=True)
                            for dataordereddict in TMserialize_data.data:
                                for key, val in dataordereddict.items():
                                    if str(key) == 'testparameterid':
                                        key = 'id'
                                    datadict[key] = val
                            datadict['ParameterId'] = testparamdetails[0]
                            if testparamdetails[1] is not None:
                                datadict['createddate'] = testparamdetails[1]
                            else:
                                datadict['createddate'] = testparamdetails[1]
                            datadict['Value'] = testparamdetails[2]
                            datadict['SessionId'] = testparamdetails[3]
                            datadict['TestParamDetailSessionDetailId'] = testparamdetails[4]
                            datadict['TestParamDetailID'] = testparamdetails[5]
                            datadict['RuleId'] = ruleid
                            datadict['ModifiedDate'] = testparamdetails[6]
                            resultList.append(datadict)
                output = create_success('fetched Test Parameter for selected rule id',resultList)
            except Exception as e:
                self.logger.error("invalid rule id."+str(e))
                return JsonResponse(create_failure(500, 'invalid rule id', 'Fail'))
        except Exception as e:
            self.logger.error("Occured error while fetching test for selected sub process id : "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(output)

###################### SPRINT - 2 STARTS ###############################

class get_captions_of_column_mapping(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getCaptionsOfColumnMapping API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getCaptionsOfColumnMapping API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            tableName = request.data['table_name']
        except Exception as e:
            self.logger.error("invalid table name"+str(e))
            return JsonResponse(create_failure(400, 'Provide table_name', 'Fail'))

        try:
            clientId = request.data['client_id']
        except Exception as e:
            self.logger.error("invalid client id"+str(e))
            return JsonResponse(create_failure(400, 'Provide client_id', 'Fail'))
        try:
            resultList = []
            resultData = models.ExcelImportMappingDetail.objects.filter(tablename = tableName,
                    customercode=clientId).values_list('excelcolumncaption','sqlcolumncaption','tablename')
            try:
                if not resultData.exists():
                    return JsonResponse(create_success("column mapping detail not available for selected table name.",[]))
                dataList = []
                for resultDataItem in resultData:
                    dataDict = {'ExcelColumnCaption':resultDataItem[0],'SQLColumnCaption':resultDataItem[1],'TableName':resultDataItem[2]}    
                    dataList.append(dataDict)
                return JsonResponse(create_success('fetched column captions for selected table name.',dataList))
            except Exception as e:
                return JsonResponse(create_failure(400,"column mapping detail not available for selected table name.","Fail"))
        except Exception as e :
            return JsonResponse(create_failure(500,"Bad Request","Fail"))


class get_all_test_list(APIView):   
    def __init__(self):
        self.logger = get_logger()
    
    def get(self, request : Request) -> JsonResponse :
        return JsonResponse({"Message":"Method Get Is Not Allowed While Api Is Working"})
 
    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getAllTestList API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getAllTestList API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            sessionId = request.data['session_id']
        except Exception as e:
            self.logger.error("invalid table name"+str(e))
            return JsonResponse(create_failure(400, 'provide session_id', 'Fail'))
        try:
            sessionDetailresult = models.SessionDetail.objects.filter(sessionid=sessionId).values_list('ruledetailsid', flat = True).distinct()
            ruleIDList=[]
            if len(sessionDetailresult) == 0 :
                return JsonResponse(create_success("No Content",[]))
            for sessionDetailresultItem in sessionDetailresult:
                ruledetails = models.Ruledetails.objects.filter(ruledetailsid=sessionDetailresultItem).values_list('ruleid',flat=True).distinct()
                for ruledetailsId in ruledetails:
                    ruleIDList.append(ruledetailsId)
            rulemasterDetailList = []
            for ruleID in ruleIDList:
                rulemasterdata = models.Rulemaster.objects.filter(rulemasterid=ruleID).values_list('processid','testno','testname').distinct()
                for rulemasterDatadetail in rulemasterdata:
                    rulemasterDetailList.append(rulemasterDatadetail)
            processDetailsList = []
            for processid in rulemasterDetailList:
                processDetails = models.Processmaster.objects.filter(processmasterid=processid[0]).values_list('processname',
                        'subprocessname').distinct()
                for processDetailsData in processDetails:
                    processDetailsList.append(processDetailsData)
            allTestList = []
            for ruledetailsid,ruleid,test,process in zip(sessionDetailresult,ruleIDList,rulemasterDetailList,processDetailsList):
                dataDict = {"TestNo":test[1],"ProcessName":process[0],"SubProcessName":process[1],"TestName":test[2],
                            "RuleDetailsID":ruledetailsid,"RuleID":ruleid}
                allTestList.append(dataDict)
            if len(allTestList) > 0 :
                return JsonResponse(create_success("fetched test list for selected session id",allTestList))
            else:
                return JsonResponse(create_success("No Content",[]))
        except Exception as e :
            self.logger.error("Error in getAllTestList Api"+str(e))
            return JsonResponse(create_failure(500,"Bad Request","Fail"))


class get_column_mapping_for_selected_table(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Message" : "Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getColumnMappingForSelectedTable API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getColumnMappingForSelectedTable API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            tableName = request.data['table_name']
        except Exception as e:
            self.logger.error("invalid table name"+str(e))
            return JsonResponse(create_failure(500, 'provide table name', 'Fail'))

        try:
            resultList = []
            resultData = models.ExcelImportMappingDetail.objects.filter(tablename = tableName).values_list('excelcolumncaption','sqlcolumncaption')
            try:
                if not resultData:
                    return JsonResponse(create_success("column captions detail not available for selected table name.",[]))
                dataList = []
                for resultDataItem in resultData:
                    dataDict = {'ExcelColumnCaption':resultDataItem[0],'SQLColumnCaption':resultDataItem[1]}    
                    dataList.append(dataDict)
                return JsonResponse(create_success('fetched column mapping detail for selected table name.',dataList))
            except Exception as e:
                self.logger.error("column mapping detail not available for selected table name."+str(e))
                return JsonResponse(create_failure(400,"column mapping detail not available for selected table name.","Fail"))
        except Exception as e :
            self.logger.error("Error in GetColumnMappinForSelectedId"+str(e))
            return JsonResponse(create_failure(400,"Bad Request.","Fail"))


class save_column_mappings_on_mapping_main(APIView):
    def __init__(self):
        self.logger = get_logger()
    
    def get(self, request : Request) -> JsonResponse :
        return JsonResponse({"Message":"Method Get Is Not Allowed While Api Is Working"})
    
    def create_bulk_column_mapping(self, request, tableId):
        columnmappingList = request.data['column_mapping_list']
        todaydate = datetime.datetime.today()
        try:
            for dictitems in columnmappingList:
                try:
                    for key in dictitems:
                        if key.lower() == 'excelcolumncaption':
                            excelcolumncaption = dictitems[key]
                        if key.lower() == 'sqlcolumncaption':
                            sqlcolumncaption = dictitems[key]
                        if key.lower() == 'isactive':
                            isactive = dictitems[key]
                        if key.lower() == 'tablename':
                            tablename = dictitems[key]
                        if key.lower() == 'customercode':
                            customercode = dictitems[key]
                        unique_id = uuid.uuid4()
                    updatetablemapping = models.ExcelImportMappingDetail(excelimportmappingdetailid=unique_id, excelcolumncaption=excelcolumncaption,
                                sqlcolumncaption=sqlcolumncaption, tablename=tablename, customercode=customercode, isactive=isactive, pid=tableId,
                                createddate=todaydate, modifieddate=todaydate)
                    updatetablemapping.save()
                except Exception as e:
                    self.logger.error("Error in saveColumnMappingsOnMappingMain API table is not added: "+str(e))
                    return JsonResponse(create_failure(500, 'column mapping insertion failed.', 'Fail'))
        except Exception as e:
            self.logger.error("Error in saveColumnMappingsOnMappingMain API table is not added: "+str(e))
            return JsonResponse(create_failure(500, 'Bad Request.', 'Fail'))
        return JsonResponse(create_success("column mapping is inserted"))
        
    def insertintotable(self, request):
        table_name = request.data['table_name']
        client_id = request.data['client_id']
        sector_id = request.data['sector_id']
        try:
            uniqueid = uuid.uuid4()
            todaydate = datetime.datetime.today()
            excelImportMain = models.Excelimportmappingmain(excelimportmappingmainid=uniqueid, tablename=table_name,
                                customercode=client_id, sector=sector_id, createddate=todaydate, modifieddate=todaydate)
            excelImportMain.save()
            if excelImportMain:
                # self.create_bulk_column_mapping(request, exceldata)
                self.create_bulk_column_mapping(request, excelImportMain.excelimportmappingmainid)
            else:
                self.logger.error("Error in saveColumnMappingsOnMappingMain API table is not added: ")
                return JsonResponse(create_failure(500, 'table is not added', 'Fail'))
        except Exception as e:
            self.logger.error("Occured error while adding table for column mapping:: "+str(e))
            return JsonResponse(create_failure(500, 'Bad Request', 'Fail'))

    def modify_table(self, request):
        table_name = request.data['table_name']
        client_id = request.data['client_id']
        sector_id = request.data['sector_id']
        colmappinglist = request.data['column_mapping_list']
        todaydate = datetime.datetime.today()
        try:
            excelImporttable = models.Excelimportmappingmain.objects.get(tablename=table_name,
                                        customercode=client_id, sector=sector_id)
            excelImporttable.modifieddate = todaydate
            excelImporttable.save()
            if excelImporttable.excelimportmappingmainid:
                tableid = excelImporttable.excelimportmappingmainid
                # delete and load
                deletetable = models.ExcelImportMappingDetail.objects.filter(tablename=table_name, customercode=client_id).delete()
                self.create_bulk_column_mapping(request, tableid)
            else:
                self.logger.error("Occured error while modifying table for column mapping:: "+str(e))
                return JsonResponse(create_failure(500, 'table is not updated', 'Fail'))
        except Exception as e:
            self.logger.error("Occured error while modifying table for column mapping:: "+str(e))
            return JsonResponse(create_failure(500, 'Bad Request', 'Fail'))
 
    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in saveColumnMappingsOnMappingMain API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in saveColumnMappingsOnMappingMain API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            table_name = request.data['table_name']
        except Exception as e:
            self.logger.error("invalid table_name"+str(e))
            return JsonResponse(create_failure(400, 'provide table_name', 'Fail'))
        try:
            client_id = request.data['client_id']
        except Exception as e:
            self.logger.error("invalid client_id"+str(e))
            return JsonResponse(create_failure(400, 'provide client_id', 'Fail'))
        try:
            sector_id = request.data['sector_id']
        except Exception as e:
            self.logger.error("invalid sector_id"+str(e))
            return JsonResponse(create_failure(400, 'provide sector_id', 'Fail'))
        try:
            column_mapping_list = request.data['column_mapping_list']
        except Exception as e:
            self.logger.error("invalid column_mapping_list: "+str(e))
            return JsonResponse(create_failure(400, 'provide column_mapping_list', 'Fail'))   
        try:
            excelmappingall = models.Excelimportmappingmain.objects.filter(tablename=table_name, customercode=client_id,
                                sector=sector_id)
            excelmappingdata = ExcelimportmappingmainSerializer(excelmappingall, many=True)
            datadict = excelmappingdata.data
            if len(datadict) > 0:
                self.modify_table(request)
            else:
                self.insertintotable(request)
        except Exception as e :
            self.logger.error("Error in saveColumnMappingsOnMappingMain Api"+str(e))
            return JsonResponse(create_failure(500,"Bad Request","Fail"))
        return JsonResponse(create_success("column mapping is inserted"))


class update_status_pending_for_selected_id(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Msg":"Method Get Is Not Allowed Here While Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in updateStatusPendingForSelectedID API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in updateStatusPendingForSelectedID API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            testIds = request.data['test_ids']
        except Exception as e:
            self.logger.error("provide test Id"+str(e))
            return JsonResponse(create_failure(400, 'provide test_id', 'Fail'))
        try:
            updateStatus = []
            try:
                for testDd in testIds:
                    todolistUpdate = Todolist.objects.filter(id=testDd).update(status='Pending', failedreason='')
                    updateStatus.append(todolistUpdate)
                if len(updateStatus) == 0:
                    return JsonResponse(create_failure(500,'Unable to set status pending for selected test id','Fail')) 
            except Exception as e:
                self.logger.error("Error in updatestatus API" + str(e))
                return JsonResponse(create_failure(500,'Bad Request','Fail'))
        except Exception as e:
            self.logger.error("Error in updatestatus API" + str(e))
            return JsonResponse(create_failure(500,'Bad Request','Fail'))
        return JsonResponse(create_success('Set Status Pending for selected Test ID',updateStatus))
             

class update_test_parameter_detail(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({"Msg":"Method Get Is Not Allowed Here While Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in updateTestParameterDetail API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in updateTestParameterDetail API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            testperameterDetails =request.data['test_parameter_details']
        except Exception as e:
            self.logger.error("provide test Id"+str(e))
            return JsonResponse(create_failure(400, 'Please Provid valid details', 'Fail'))
        try:    
            for testperameterDetailsData in testperameterDetails:
                try:
                    todaydate = datetime.datetime.today()
                    uniqueId = uuid.uuid4()
                    testPerameterUpdate = models.Testparameterdetail(testparameterdetailid=uniqueId,parameterid=testperameterDetailsData['ID'],
                            value=testperameterDetailsData['Value'],ruledetailsid=testperameterDetailsData['RuleDetailsID'],
                            sessionid=testperameterDetailsData['SessionID'],sessiondetailid=testperameterDetailsData['SessionDetailID'],
                            createddate=todaydate,modifieddate=todaydate)
                    testPerameterUpdate.save()
                except Exception as e : 
                    self.logger.error("Error in UpdateTestParameterDetails"+str(e))
        except Exception as e:
            self.logger.error("Error in UpdateTestParameterDetails"+str(e))
            return JsonResponse(create_failure(500,'Bad Request','Fail'))
        return JsonResponse(create_success('Test parameter is updated',[]))


class get_power_bi_url(APIView):   
    def __init__(self):
        self.logger = get_logger()
    
    def get(self, request : Request) -> JsonResponse :
        return JsonResponse({"Message":"Method Get Is Not Allowed While Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getPowerBIURL API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getPowerBIURL API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            ruleId = request.data['rule_id']
        except Exception as e:
            self.logger.error("invalid rule_id"+str(e))
            return JsonResponse(create_failure(400, 'provide rule_id', 'Fail'))

        try:
            templateMappingList = []
            templateMappingDetails = models.TestClientTemplateMapping.objects.filter(ruleid=ruleId).values_list(
            'testclienttemplatemappingid','clientid','testno','dashboardtype','templatefilename',
            'templatesourcefilename','createdby','createddate','modifiedby','modifieddate','exeversionno',
            'modulename','enterdonmachineid','sysmodifieddatetime','publisheddatetime','sector','ruleid','url'
            )
            for templateMappingDetail in templateMappingDetails:
                templatemapping = {"ID":templateMappingDetail[0],"ClientID":templateMappingDetail[1],
                "TestNo":templateMappingDetail[2],"DashboardType":templateMappingDetail[3],
                "TemplateFileName":templateMappingDetail[4],"TemplateSourceFileName":templateMappingDetail[5],
                "CreatedBy":templateMappingDetail[6],"CreatedDate":templateMappingDetail[7],
                "ModifiedBy":templateMappingDetail[8],"ModifiedDate":templateMappingDetail[9],
                "ExeVersionNo":templateMappingDetail[10],"ModuleName":templateMappingDetail[11],
                "EnteredOnMachineID":templateMappingDetail[12],"SysModifiedDateTime":templateMappingDetail[13],
                "PublishedDateTime":templateMappingDetail[14],"Sector":templateMappingDetail[15],
                "RuleID":templateMappingDetail[16],"URL":templateMappingDetail[17]}
                templateMappingList.append(templatemapping)
        except Exception as e:
            self.logger.error("invalid table name"+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(create_success('fetched powerbi url for selected rule id.',templateMappingList))


class get_table_data_for_date_range(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.connection = db_conn()
    
    def get(self, request : Request) -> JsonResponse :
        return JsonResponse({"Message":"Method Get Is Not Allowed While Api Is Working"})

    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in GetTableDataForDateRange API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in GetTableDataForDateRange API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            dbName = request.data['database_name']
        except Exception as e:
            self.logger.error("invalid database_name"+str(e))
            return JsonResponse(create_failure(400, 'provide database_name', 'Fail'))
        try:
            table_name = request.data['table_name']
        except Exception as e:
            self.logger.error("invalid table_name"+str(e))
            return JsonResponse(create_failure(400, 'provide table_name', 'Fail'))
        try:
            start_date = request.data['start_date']
        except Exception as e:
            self.logger.error("invalid start_date"+str(e))
            return JsonResponse(create_failure(400, 'provide start_date', 'Fail'))
        try:
            end_date = request.data['end_date']
        except Exception as e:
            self.logger.error("invalid end_date"+str(e))
            return JsonResponse(create_failure(400, 'provide end_date', 'Fail'))
        try:
            column_name = request.data['column_name']
        except Exception as e:
            self.logger.error("invalid column_name"+str(e))
            return JsonResponse(create_failure(400, 'provide column_name', 'Fail'))
        try:
            rule_id = request.data['rule_id']
        except Exception as e:
            self.logger.error("invalid rule_id"+str(e))
            return JsonResponse(create_failure(400, 'provide rule_id', 'Fail'))
        try:
            session_id = request.data['session_id']
        except Exception as e:
            self.logger.error("invalid session_id"+str(e))
            return JsonResponse(create_failure(400, 'provide session_id', 'Fail'))
        try:
            resultset = {}
            query = get_table_data_for_date_range_sql(dbName, table_name, start_date, end_date, column_name)
            self.logger.info("query: "+ str(query))
            cursor = self.connection.cursor()
            queryset = cursor.execute(query).fetchall()
            if not queryset:
                return JsonResponse(create_failure(400, 'Error in running the query', 'Fail'))
            else:
                if queryset[0][0] == 0:
                    resultset['TableRecords'] = False
                else:
                    resultset['TableRecords'] = True
            self.connection.close()
        except Exception as e:
            self.logger.error("invalid provided parameters"+str(e))
            if "Conversion failed" in str(e):
                return JsonResponse(create_failure(400, 'Conversion Failed. Invalid Column Type', 'Fail'))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        # Update/Insert in TestParameterDetail table
        try:
            todaydate = datetime.datetime.today()
            parameterList = ['column_name','start_date', 'end_date']
            for ruleid in rule_id:
                ruledetailsidlist = models.Ruledetails.objects.filter(ruleid=ruleid).values_list('ruledetailsid')
                if ruledetailsidlist.exists():
                    ruledetailsid = ruledetailsidlist[0][0]
                else:
                    self.logger.info("No Rule Details ID for ruleid: "+str(rule_id))
                    continue
                testparamdetailsdata = models.Testparameterdetail.objects.filter(sessionid=session_id, ruledetailsid=ruledetailsid)
                if testparamdetailsdata.exists():
                    testparamupdate = models.Testparameterdetail.objects.filter(sessionid=session_id, ruledetailsid=ruledetailsid).update(
                        modifieddate=todaydate)
                else:
                    for param in parameterList:
                        parameteridlist = models.Testparameter.objects.filter(ruledetailsid=ruledetailsid, parametername=param).values_list(
                                "testparameterid")
                        if parameteridlist.exists():
                            parameterid = parameteridlist[0][0]
                        else:
                            self.logger.info("No Parameter ID for selected ruleDetails ID: "+str(ruledetailsid))
                            continue
                        testparamdetailsID = uuid.uuid4()
                        testparaminsert = models.Testparameterdetail(createddate=todaydate, modifieddate=todaydate, value=request.data[param],
                            sessionid=session_id, ruledetailsid=ruledetailsid, testparameterdetailid=testparamdetailsID, parameterid=parameterid)
                        testparaminsert.save()
        except Exception as e:
            self.logger.error("invalid provided parameters"+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(create_success('fetched status for records',resultset))


class get_risk_controls_for_selected_subprocess_id(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.connection = db_conn()
    
    def post(self, request: Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in getRiskControlsForSelectedSubprocessId API token: ")
                return JsonResponse(create_failure(400, 'invalid Token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getRiskControlsForSelectedSubprocessId API token: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid Token', 'Fail'))
        try:
            subprocessId = request.data['subprocess_id']
            riskIdDic = dict()
            for subprocessIdVar in subprocessId:
                try:
                    riskMasterObject = Riskmaster.objects.filter(processid=subprocessIdVar)
                    riskMasterData = RiskMasterSerializer(riskMasterObject, many=True)
                    if riskMasterObject.exists():
                        try:
                            for riskMasterRecord in riskMasterData.data:
                                try:
                                    if(riskMasterRecord['riskdetailid'] != None):
                                        riskIdDic[riskMasterRecord['id']] = riskMasterRecord['riskdetailid']
                                except Exception as e:
                                    self.logger.error("Error in RiskMaster Table: "+str(e))
                                    return JsonResponse(create_failure(500, 'Error in RiskMaster Table', 'Fail'))
                        except Exception as e:
                            self.logger.error("Error in RiskMaster Table: "+str(e))
                            return JsonResponse(create_failure(500, 'Error in RiskMaster Table', 'Fail'))
                except Exception as e:
                    self.logger.error("Error in RiskMaster Table: "+str(e))
                    return JsonResponse(create_failure(500, 'Error in RiskMaster Table', 'Fail'))
            
            riskDetailsList = []
            for riskIdVar in riskIdDic.keys():
                try:
                    riskDetailObject = Riskdetail.objects.filter(id=riskIdDic[riskIdVar]) 
                    riskDetailData = RiskDetailSerializer(riskDetailObject, many=True)
                    riskInfoJson = dict()
                    if riskDetailObject.exists():
                        try:
                            for riskDetailRecord in riskDetailData.data:
                                try:
                                    flag = 0
                                    for pos,var in enumerate(riskDetailsList):
                                        try:
                                            if(var['ID'] == riskDetailRecord['riskl1id']):
                                                riskDetailsList[pos]['RiskId'].append(riskIdVar)
                                                childResponse = self.child_call(riskIdVar,riskDetailRecord)
                                                if(childResponse == False):
                                                    return JsonResponse(create_failure(500, 'Error in Control Table', 'Fail'))
                                                riskDetailsList[pos]['Child'].append(childResponse)
                                                flag = 1
                                                break
                                        except Exception as e:
                                            self.logger.error("Error in Control Table: "+str(e))
                                            return JsonResponse(create_failure(500, 'Error in Control Table', 'Fail'))
                                    if(flag == 0):    
                                        riskInfoJson['RiskId'] = []                                    
                                        riskInfoJson['RiskId'].append(riskIdVar)
                                        riskInfoJson['ID'] = riskDetailRecord['riskl1id']
                                        riskInfoJson['Risk1Level'] = riskDetailRecord['riskl1name']
                                        riskInfoJson['Risk1Description'] = riskDetailRecord['riskl1description']
                                        riskInfoJson['IsExpand'] = True
                                        riskInfoJson['Child'] = []
                                        childResponse = self.child_call(riskIdVar,riskDetailRecord)
                                        if(childResponse == False):
                                            return JsonResponse(create_failure(500, 'Error in Control Table', 'Fail'))
                                        riskInfoJson['Child'].append(childResponse)
                                except Exception as e:
                                    self.logger.error("Error in RiskDetail Table: "+str(e))
                                    return JsonResponse(create_failure(500, 'Error in RiskDetail Table', 'Fail'))
                        except Exception as e:
                            self.logger.error("Error in RiskDetail Table: "+str(e))
                            return JsonResponse(create_failure(500, 'Error in RiskDetail Table', 'Fail'))
                    if(len(riskInfoJson) != 0):
                        riskDetailsList.append(riskInfoJson)
                except Exception as e:
                    self.logger.error("Error in RiskDetail Table: "+str(e))
                    return JsonResponse(create_failure(500, 'Error in RiskDetail Table', 'Fail'))
        except Exception as e:
            self.logger.error("Error in getRiskControlsForSelectedSubprocessId API: "+str(e))
            return JsonResponse(create_failure(500, 'Error in getRiskControlsForSelectedSubprocessId API', 'Fail'))
        return JsonResponse(create_success('fetched status for records',riskDetailsList))


    def child_call(self,riskIdVar,riskDetailRecord):
        try:
            riskChildJson = dict()
            riskChildJson['RiskId'] = riskIdVar
            riskChildJson['ID'] = riskDetailRecord['riskl2id']
            riskChildJson['Risk2Level'] = riskDetailRecord['riskl2name']
            riskChildJson['Risk2Description'] = riskDetailRecord['riskl2description'] 
            riskChildJson['IsExpand'] = True
            riskChildJson['Child'] = []   
            riskControlObject = Riskcontrol.objects.filter(riskl2id=riskChildJson['ID'])
            riskControlData = RiskControlSerializer(riskControlObject, many=True)
            if riskControlObject.exists():
                try:
                    for riskControlRecord in riskControlData.data:
                        try:
                            riskControlJson = dict()
                            riskControlJson['ID'] = riskControlRecord['id']
                            riskControlJson['ControlName'] = riskControlRecord['controlname']
                            riskControlJson['ControlDescription'] = riskControlRecord['controldescription']
                            riskChildJson['Child'].append(riskControlJson)
                        except Exception as e:
                            self.logger.error("Error in Control Table: "+str(e))
                            return False
                except Exception as e:
                    self.logger.error("Error in Control Table: "+str(e))
                    return False
            return riskChildJson
        except Exception as e:
            self.logger.error("Error in Control Table: "+str(e))
            return False
