from django.test import TestCase
from dashboard.models import *

class test_models(TestCase):
    
    def set_up(self):
        # Settings 1
        self.TestDataSettings = Settings.objects.create(settingsid = '2', wsurl = 'Technical',exeupdateurl='/expupdateurl',createdby='dilip')

        # Sectormaster 2
        self.TestDataSectormaster = Sectormaster.objects.create(sectormasterid = '12', sector = 'Sector1',lefticonimagename='imageName',lefticonlablecaption='CaptionTesting')

        # Usertosectormapping 3
        self.TestDataUsertosectormapping = Usertosectormapping.objects.create(usertosectorid = '01', userid = 'USER06',sectorid='01S',createdby='jhon doe')

        # Clientmaster 4
        self.TestDataClientmaster = Clientmaster.objects.create(clientmasterid = '10', clientname = 'client01',clientcode='01C',sector='generalSector')

        # Usertoclientmapping 5
        self.TestDataUsertosectormapping = Usertoclientmapping.objects.create(userclientmappingid = '01', clientid = '01C',userid='uid01',createdby='vishal')

        # Clienttoprocessmapping 6
        self.TestDataClienttoprocessmapping= Clienttoprocessmapping.objects.create(clientprocessmappingid = '06', clientid = '06C',processid='pid06',createdby='random user')
        
        # Processmaster 7
        self.TestDataProcessmaster= Processmaster.objects.create(processmasterid = '07', processname = 'process07',subprocessname='subprocess07',pid='07')

        # Sessionmain 8
        self.TestDataSessionmain= Sessionmain.objects.create(sessionmainid = '08', clientid = 'client08',clientcode='client08',sessionno='08')

        # TblMDatabasesettings 9
        self.TestDataTblMDatabasesettings= TblMDatabasesettings.objects.create(databasesettingsid = '09', databasename = 'digicube',databasetype='tabuler',servername='express')

        # Rulemaster 10
        self.TestDataRulemaster= Rulemaster.objects.create(rulemasterid = '10', subprocessname = 'subprocess10',testno='10',testname='test10')

        # Clienttosubprocessmapping 11
        self.TestDataClienttosubprocessmapping= Clienttosubprocessmapping.objects.create(clientsubprocessmappingid = '11', clientid = '11',subprocessid='11',createdby='jhon doe')

        # Testparameter 12
        self.TestDataTestparameter= Testparameter.objects.create(testparameterid = '12', ruledetailsid = '12',parametername = 'dataParam', parameterdatatype = 'json',isbold=0,isitalic=0,isunderline=0,isstrikeout=0)

        # Ruledetails 13
        self.TestdataRuledetails= Ruledetails.objects.create(ruledetailsid = '13', ruleid = '13',sequenceno = '13', subprocesscaption = 'subprocessnumber13')

        # Testparameterdetail 14
        self.TestDataTestparameterdetail= Testparameterdetail.objects.create(testparameterdetailid = '14', parameterid = '14',value = '14', ruledetailsid = 'detailid14')

        # ExcelImportMappingDetail 15
        self.TestDataExcelImportMappingDetail= ExcelImportMappingDetail.objects.create(excelimportmappingdetailid = '15', excelcolumncaption = 'excelmapping15',sqlcolumncaption = 'captionsuccess15', pid = 'pid15')

        # SessionDetail 16
        self.TestDataSessionDetail= SessionDetail.objects.create(sessiondetailid = '16', sessionid = 'sessionid16',testno = 'test16', ruledetailsid = 'rid16')
        
        # Excelimportmappingmain 17
        self.TestDataExcelimportmappingmain= Excelimportmappingmain.objects.create(excelimportmappingmainid = '17', tablename = 'Scs_table',customercode = '17', sector = 'sector17')
    
        # TestClientTemplateMapping 18
        self.TestDataTestClientTemplateMapping= TestClientTemplateMapping.objects.create(testclienttemplatemappingid = '18',
         clientid = 'clientid18',testno = 'test18', dashboardtype = 'rid18')
        
        # Risk Control 19
        self.TestDataRiskControl= Riskcontrol.objects.create(id = 'rl1.1.1',riskl2id = 'rl1.1',controlname = 'Control 1.1.1', controldescription = '1.1.1 Control Description')
        # Risk Master 20
        self.TestDataRiskMaster= Riskmaster.objects.create(id = 'r5',processid = 'WAM_03_2',risk = 'Risk 5', riskdetails = 'Risk Detail 5')
        # Risk Detail 21
        self.TestDataRiskDetail= Riskdetail.objects.create(id = 'rd1',riskl1id = 'rl1',riskl1name = 'Risk1Level', riskl1description = 'Risk 1 Description',riskl2id = 'rl2',riskl2name = 'Risk2Level', riskl2description = 'Risk 2 Description')

    
    def test_TestClientTemplateMapping_models(self):
        objects = TestClientTemplateMapping.objects.get(sessiondetailid = '18')
        self.assertEqual(objects.sessiondetailid, '18')
        self.assertEqual(objects.sessionid, 'clientid18')
        self.assertEqual(objects.testno, 'test18')
        self.assertEqual(objects.ruledetailsid, 'rid18')

    def test_Excelimportmappingmain_models(self):
        objects = Excelimportmappingmain.objects.get(excelimportmappingmainid = '17')
        self.assertEqual(objects.excelimportmappingmainid, '17')
        self.assertEqual(objects.tablename, 'Scs_table')
        self.assertEqual(objects.customercode, '17')
        self.assertEqual(objects.sector, 'sector17')
        
    def test_SessionDetail_models(self):
        objects = SessionDetail.objects.get(sessiondetailid = '16')
        self.assertEqual(objects.sessiondetailid, '16')
        self.assertEqual(objects.sessionid, 'sessionid16')
        self.assertEqual(objects.testno, 'test16')
        self.assertEqual(objects.ruledetailsid, 'rid16')

    def test_ExcelImportMappingDetail_models(self):
        objects = ExcelImportMappingDetail.objects.get(excelimportmappingdetailid = '15')
        self.assertEqual(objects.excelimportmappingdetailid, '15')
        self.assertEqual(objects.excelcolumncaption, 'excelmapping15')
        self.assertEqual(objects.sqlcolumncaption, 'captionsuccess15')
        self.assertEqual(objects.pid, 'pid15')

    def test_Testparameterdetail_models(self):
        objects = Testparameterdetail.objects.get(testparameterdetailid = '14')
        self.assertEqual(objects.testparameterdetailid, '14')
        self.assertEqual(objects.parameterid, '14')
        self.assertEqual(objects.value, '14')
        self.assertEqual(objects.ruledetailsid, 'detailid14')

    def test_Ruledetails_models(self):
        objects = Ruledetails.objects.get(ruledetailsid = '13')
        self.assertEqual(objects.ruledetailsid, '13')
        self.assertEqual(objects.ruleid, '13')
        self.assertEqual(objects.sequenceno, 13)
        self.assertEqual(objects.subprocesscaption, 'subprocessnumber13')

    def test_Testparameter_models(self):
        objects = Testparameter.objects.get(testparameterid = '12')
        self.assertEqual(objects.testparameterid, '12')
        self.assertEqual(objects.ruledetailsid, '12')
        self.assertEqual(objects.parametername, 'dataParam')
        self.assertEqual(objects.parameterdatatype, 'json')

    def test_Clienttosubprocessmapping_models(self):
        objects = Clienttosubprocessmapping.objects.get(clientsubprocessmappingid='11')
        self.assertEqual(objects.clientsubprocessmappingid,'11')
        self.assertEqual(objects.clientid,'11')
        self.assertEqual(objects.subprocessid,'11')
        self.assertEqual(objects.createdby,'jhon doe')

    def test_Rulemaster_models(self):
        objects = Rulemaster.objects.get(rulemasterid='10')
        self.assertEqual(objects.rulemasterid,'10')
        self.assertEqual(objects.subprocessname,'subprocess10')
        self.assertEqual(objects.testno,'10')
        self.assertEqual(objects.testname,'test10')

    def test_TblMDatabasesettings_models(self):
        objects = TblMDatabasesettings.objects.get(databasesettingsid='09')
        self.assertEqual(objects.databasesettingsid,'09')
        self.assertEqual(objects.databasename,'digicube')
        self.assertEqual(objects.databasetype,'tabuler')
        self.assertEqual(objects.servername,'express')

    def test_Sessionmain_models(self):
        objects = Sessionmain.objects.get(sessionmainid='08')
        self.assertEqual(objects.sessionmainid,'08')
        self.assertEqual(objects.clientid,'client08')
        self.assertEqual(objects.clientcode,'client08')
        self.assertEqual(objects.sessionno,'08')

    def test_Processmaster_models(self):
        objects = Processmaster.objects.get(processmasterid='07')
        self.assertEqual(objects.processmasterid,'07')
        self.assertEqual(objects.processname,'process07')
        self.assertEqual(objects.subprocessname,'subprocess07')
        self.assertEqual(objects.pid,'07')
    
    def test_Clienttoprocessmapping_models(self):
        objects = Clienttoprocessmapping.objects.get(clientprocessmappingid='06')
        self.assertEqual(objects.clientprocessmappingid,'06')
        self.assertEqual(objects.clientid,'06C')
        self.assertEqual(objects.processid,'pid06')
        self.assertEqual(objects.createdby,'random user')

    def test_Usertoclientmapping_models(self):
        objects = Usertoclientmapping.objects.get(userclientmappingid='01')
        self.assertEqual(objects.userclientmappingid,'01')
        self.assertEqual(objects.clientid,'01C')
        self.assertEqual(objects.userid,'uid01')
        self.assertEqual(objects.createdby,'vishal')

    def test_Clientmaster_models(self):
        objects = Clientmaster.objects.get(clientmasterid='10')
        self.assertEqual(objects.clientmasterid,'10')
        self.assertEqual(objects.clientname,'client01')
        self.assertEqual(objects.clientcode,'01C')
        self.assertEqual(objects.sector,'generalSector')

    def test_Usertosectormapping_models(self):
        objects = Usertosectormapping.objects.get(usertosectorid='01')
        self.assertEqual(objects.usertosectorid,'01')
        self.assertEqual(objects.userid,'USER06')
        self.assertEqual(objects.sectorid,'01S')
        self.assertEqual(objects.createdby,'jhon doe')

    def test_Sectormaster_models(self):
        objects = Sectormaster.objects.get(sectormasterid='12')
        self.assertEqual(objects.sectormasterid,'12')
        self.assertEqual(objects.sector,'Sector1')
        self.assertEqual(objects.lefticonimagename,'imageName')
        self.assertEqual(objects.lefticonlablecaption,'CaptionTesting')

    def test_Setting_models(self):
        objects = Settings.objects.get(settingsid=2)
        self.assertEqual(objects.settingsid,'2')
        self.assertEqual(objects.wsurl,'Technical')
        self.assertEqual(objects.exeupdateurl,'/expupdateurl')
        self.assertEqual(objects.createdby,'dilip')
 
    def test_RiskMaster_models(self):
        objects = Riskmaster.objects.get(id='r5')
        self.assertEqual(objects.id,'r5')
        self.assertEqual(objects.processid,'WAM_03_2')
        self.assertEqual(objects.risk,'Risk 5')
        self.assertEqual(objects.riskdetails,'Risk Detail 5')

    def test_RiskControl_models(self):
        objects = Riskcontrol.objects.get(id='rl1.1.1')
        self.assertEqual(objects.id,'rl1.1.1')
        self.assertEqual(objects.riskl2id,'rl1.1')
        self.assertEqual(objects.controlname,'Control 1.1.1')
        self.assertEqual(objects.controldescription,'1.1.1 Control Description')

    def test_RiskDetail_models(self):
        objects = Riskdetail.objects.get(id='rd1')
        self.assertEqual(objects.id,'rd1')
        self.assertEqual(objects.riskl1id,'rl1')
        self.assertEqual(objects.riskl1name,'Risk1Level')
        self.assertEqual(objects.riskl1description,'Risk 1 Description')

    

class bug_model_testing(TestCase):
    def set_up_bug(self):
        #1 bug demo Data For Model Processmaster
        self.TestDataProcessmaster= Processmaster.objects.create(processmasterid = '01', processname = 'process01',subprocessname='subprocess01',processdescription='This Is the Selected Proccess For Id')
    #1 bug fetch data For Model Processmaster    
    def test_bug_Processmaster(self):   
        objects = Processmaster.objects.get(processmasterid='01')
        self.assertEqual(objects.processmasterid,'01')
        self.assertEqual(objects.processname,'process01')
        self.assertEqual(objects.subprocessname,'subprocess01')
        self.assertEqual(objects.processdescription,'This Is the Selected Proccess For Id')

    def test_2bug_SessionMain(self):
        # setup
        self.TestDataSessionmain= Sessionmain.objects.create(sessionmainid = '11', clientid = 'client12',clientcode='client13',sessionno='14',userid='15')
        # get And Check If Value is same inserted
        objects = Sessionmain.objects.get(sessionmainid='11')
        self.assertEqual(objects.sessionmainid,'11')
        self.assertEqual(objects.clientid,'client12')
        self.assertEqual(objects.clientcode,'client13')
        self.assertEqual(objects.sessionno,'14')
        self.assertEqual(objects.userid,'15')

    
