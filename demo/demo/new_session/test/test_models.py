from django.test import TestCase
from dashboard.models import *
from runTest.models import *

class test_models(TestCase):
    
    def set_up(self):
        # Sessiontestmapping 1
        self.TestdataRuledetails= Sessiontestmapping.objects.create(sessiontestid = '11', ruledetailsid = '12',userid = '13', sessionid = '14')
        
        # Ruledetails 2
        self.TestdataRuledetails= Ruledetails.objects.create(ruledetailsid = '21', ruleid = '22',sequenceno = '23', subprocesscaption = '24subprocesscaption')
        
        # Rulemaster 3
        self.TestDataRulemaster= Rulemaster.objects.create(rulemasterid = '31', subprocessname = '32subprocessname',testno='33',testname='34testname')
    
    # Sessiontestmapping 1
    def test_Ruledetails_models(self):
        objects = Ruledetails.objects.get(sessiontestid = '11')
        self.assertEqual(objects.sessiontestid, '11')
        self.assertEqual(objects.ruledetailsid, '12')
        self.assertEqual(objects.userid, '13')
        self.assertEqual(objects.sessionid, '14')

    # Ruledetails 2
    def test_Ruledetails_models(self):
        objects = Ruledetails.objects.get(ruledetailsid = '13')
        self.assertEqual(objects.ruledetailsid, '13')
        self.assertEqual(objects.ruleid, '13')
        self.assertEqual(objects.sequenceno, 13)
        self.assertEqual(objects.subprocesscaption, 'subprocessnumber13')

    # Rulemaster 3
    def test_Rulemaster_models(self):
        objects = Rulemaster.objects.get(rulemasterid='10')
        self.assertEqual(objects.rulemasterid,'10')
        self.assertEqual(objects.subprocessname,'subprocess10')
        self.assertEqual(objects.testno,'10')
        self.assertEqual(objects.testname,'test10')   
    
    