from django.http.response import JsonResponse
from django.apps import apps
from rest_framework.views import APIView
from rest_framework.request import HttpRequest, Request

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_connection import db_conn
from common_files.create_response import create_failure, create_success
from sql_queries.new_session_sql_query import insert_record_in_tbl_m_database_table
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token

from dashboard import models as dashboardModels
from event_emitter.models import Todolist
from run_test.models import Sessiontestmapping

import json, requests, datetime, uuid, subprocess, random, string

# Create your views here.
class new_session(APIView):
    def __init__(self):
        self.logger = get_logger()
        self.config = read_config()
        dt = datetime.datetime.now()
        self.todaydate = ("{}.{:03d}".format(dt.strftime('%Y-%m-%d %I:%M:%S'), dt.microsecond//1000))

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})
    
    def create_database(self):
        try:
            self.username = self.config['DIGICUBEDB']['username']
            password = self.config['DIGICUBEDB']['password']
            self.password_varb = bytes(password,'utf-8')
            self.server = self.config['DIGICUBEDB']['server']
            print(self.username, password, self.server, self.databaseName)
            cmd = "sqlcmd -U {} -P {} -S {} -d {} -i Digicube_FS_WAM.sql -o testdb.txt".format(self.username,
                password, self.server, self.databaseName)
            returned_value = subprocess.getoutput(cmd)
        except Exception as e:
            print("exception: ",(e))
            return False
        return True

    def post(self, payload) -> JsonResponse:
        try:
            client_id = payload['ClientID']
        except Exception as e:
            self.logger.error("invalid clientID"+str(e))
            return create_failure(400, 'provide ClientID', 'Fail')
        try:
            session_id = payload['SessionID']
        except Exception as e:
            self.logger.error("invalid SessionID"+str(e))
            return create_failure(400, 'provide SessionID', 'Fail')
        try:
            AuditFrom = payload['AuditFrom']
        except Exception as e:
            self.logger.error("invalid AuditFrom "+str(e))
            return create_failure(400, 'provide AuditFrom', 'Fail')
        try:
            AuditTo = payload['AuditTo']
        except Exception as e:
            self.logger.error("invalid AuditTo "+str(e))
            return create_failure(400, 'provide AuditTo', 'Fail')
        try:
            ProjectName = payload['ProjectName']
        except Exception as e:
            self.logger.error("invalid ProjectName "+str(e))
            return create_failure(400, 'provide ProjectName', 'Fail')
        try:
            serialno = payload['SerialNo']
        except Exception as e:
            self.logger.error("invalid serialno "+str(e))
            return create_failure(400, 'provide serialno', 'Fail')
        try:
            userid = payload['userid']
        except Exception as e:
            self.logger.error("invalid userid "+str(e))
            return create_failure(400, 'provide valid token', 'Fail')
        try:
            # Step- I Create new database)
            try:
                self.databaseName = datetime.datetime.now().strftime("%B%d%Y%H%M%S")
                self.logger.debug("db name :"+ str(self.databaseName))
                self.connection = db_conn()
                self.connection.autocommit = True
                cursor = self.connection.cursor()
                db_create = cursor.execute("create database "+str(self.databaseName))
                cursor.close()
                self.connection.close()
                create_db = self.create_database()
            except Exception as e:
                self.logger.error("error in creating db: "+str(e))
                return create_failure(400, 'Error in creating database', 'Fail')

            #STEP-II: insert record in Tbl_m_databases table
            try:
                self.tbldbSettingsId = str(uuid.uuid4())
                password = self.config['DIGICUBEDB']['password']
                self.logger.debug("tbldbSettingsId: "+ str(self.tbldbSettingsId))
                self.connection = db_conn()
                self.connection.autocommit = True
                cursor = self.connection.cursor()
                insertIntoTable = cursor.execute(insert_record_in_tbl_m_database_table(self.tbldbSettingsId,self.databaseName,'SQL',self.server,self.username,'1',str(self.todaydate),password))
                cursor.close()
                self.connection.close()
            except Exception as e:
                self.logger.error("Error in Tbl_m_databasessettings table: "+str(e))
                self.connection = db_conn()
                self.connection.autocommit = True
                cursor = self.connection.cursor()
                db_drop = cursor.execute("drop database "+str(self.databaseName))
                cursor.close()
                self.connection.close()
                return create_failure(400, 'Error in creating Tbl_m_databasessettings table', 'Fail')
            
            # Step-III: Insert new record in session main table
            try:
                clientCode = ''
                sessionNum = result_str = ''.join(random.choice(string.ascii_letters) for i in range(10))
                sessionMainId = uuid.uuid4()
                self.logger.debug("sessionMainId: "+ str(sessionMainId))
                clientCodelist = dashboardModels.Clientmaster.objects.filter(clientmasterid=client_id).values_list("clientcode")
                for item in clientCodelist:
                    clientCode = item[0]
                self.sessionMainTbl = dashboardModels.Sessionmain(sessionmainid=sessionMainId, clientid=client_id,
                            dbid=self.tbldbSettingsId, sessionstartdate=self.todaydate, createddate=self.todaydate,
                            auditfrom=AuditFrom, auditto=AuditTo, projectname=ProjectName, serialno=serialno, 
                            sessionno=sessionNum, clientcode=clientCode, userid=userid)
                self.sessionMainTbl.save()
            except Exception as e:
                self.logger.error("Error in creating sessionMainTbl: "+str(e))
                self.connection = db_conn()
                self.connection.autocommit = True
                cursor = self.connection.cursor()
                db_drop = cursor.execute("drop database "+str(self.databaseName))
                deleteFromTable = cursor.execute("DELETE FROM tbl_m_DatabaseSettings WHERE ID='"+self.tbldbSettingsId+"' ")
                cursor.close()
                self.connection.close()
                return create_failure(400, 'Error in creating sessionMainTbl', 'Fail')

            #Step - IV : update client master table
            try:
                clientMaster = dashboardModels.Clientmaster.objects.get(clientmasterid=client_id)
                clientMaster.sessionid = self.sessionMainTbl.sessionmainid
                clientMaster.save()
            except Exception as e:
                self.logger.error("Error in creating sessionMainTbl: "+str(e))
                self.connection = db_conn()
                self.connection.autocommit = True
                cursor = self.connection.cursor()
                db_drop = cursor.execute("drop database "+str(self.databaseName))
                deleteFromTable = cursor.execute("DELETE FROM tbl_m_DatabaseSettings WHERE ID='"+self.tbldbSettingsId+"' ")
                cursor.close()
                self.connection.close()
                self.sessionMainTbl.delete()
                return create_failure(400, 'Error in creating sessionMainTbl', 'Fail')
        except Exception as e:
            self.logger.error("Error in new_session API: "+str(e))
            return create_failure(400, 'new_session API Fail', 'Fail')
        return create_success('success')


class view_results(APIView):
    def __init__(self):
        self.logger = get_logger()

    def get(self, request: Request) -> JsonResponse:
        return JsonResponse({})
    
    def post(self, request:Request) -> JsonResponse:
        try:
            userid = verify_jwt_token(request.META['HTTP_AUTHORIZATION'])
            if userid == 0:
                self.logger.error("Error in View Results API token: ")
                return JsonResponse(create_failure(400, 'Invalid token', 'Fail'))
        except Exception as e:
            self.logger.error("Error in View Results API: "+str(e))
            return JsonResponse(create_failure(400, 'Please provide valid token', 'Fail'))
        try:
            session_id = request.data['SessionID']
        except Exception as e:
            self.logger.error("invalid SessionID"+str(e))
            return JsonResponse(create_failure(400, 'invalid SessionID', 'Fail'))
        try:
            resultset = []
            testdetails = Sessiontestmapping.objects.filter(userid=userid, sessionid=session_id).values_list('ruledetailsid',
                            'todolistid','ruleid','createddate')
            if testdetails.exists():
                for mappingitems in testdetails:
                    resultdict = {}
                    try:
                        ruledetails = dashboardModels.Ruledetails.objects.filter(ruledetailsid=mappingitems[0]).values_list('shortdescription')
                        for ruledetailsitem in ruledetails:
                            resultdict['ShortDescription'] = ruledetailsitem[0]
                        rulemaster = dashboardModels.Rulemaster.objects.filter(rulemasterid=mappingitems[2]).values_list('testno', 'testname')
                        resultdict['TestNo'] = rulemaster[0][0]
                        resultdict['TestName'] = rulemaster[0][1]
                        todoliststatus = Todolist.objects.filter(id=mappingitems[1]).values_list('status')
                        resultdict['Status'] = todoliststatus[0][0]
                        resultdict['CreatedDate'] = mappingitems[3]
                        resultdict['RuleId'] = mappingitems[2]
                        resultset.append(resultdict)
                    except Exception as e:
                        self.logger.error("Occured error while fetching list of Results: "+str(e))
                        return JsonResponse(create_failure(400, 'Invalid SessionID', 'Fail'))
            else:
                return JsonResponse(create_failure(500, 'No Records Found', 'Fail'))
        except Exception as e:
            self.logger.error("Occured error while fetching list of Results: "+str(e))
            return JsonResponse(create_failure(400, 'Bad Request', 'Fail'))
        return JsonResponse(create_success('success', resultset))
