from django.test import TestCase
from runTest.models import Storedproceduretable, Pythonfunctionstable


class test_models(TestCase):
    
    def set_up(self):
        #Storedproceduretable 01
        self.StoredproceduretableTestData= Storedproceduretable.objects.create(storedproceduretableid = '01',
         ruledetailsid = 'rule01',paramname = 'spQuery', paramvalue = 'select * from Storedproceduretable')
        
        #Pythonfunctionstable 02
        self.PythonfunctionstableTestData= Pythonfunctionstable.objects.create(pythonfunctionsid = '02',
        ruledetailsid = 'rule02',taskid = 'task02', pythonfunctionname = 'getStoreProcDetails')
    
    def test_pythonfunctionstable_models(self):
        objects = Pythonfunctionstable.objects.get(pythonfunctionsid = '02')
        self.assertEqual(objects.pythonfunctionsid, '02')
        self.assertEqual(objects.ruledetailsid, 'rule02')
        self.assertEqual(objects.taskid, 'task02')
        self.assertEqual(objects.pythonfunctionname, 'getStoreProcDetails')

    def test_storedproceduretable_models(self):
        objects = Storedproceduretable.objects.get(sessiondetailid = '01')
        self.assertEqual(objects.sessiondetailid, '01')
        self.assertEqual(objects.sessionid, 'rule01')
        self.assertEqual(objects.testno, 'spQuery')
        self.assertEqual(objects.ruledetailsid, 'select * from Storedproceduretable')