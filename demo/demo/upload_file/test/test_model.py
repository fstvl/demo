from django.test import TestCase
from eventEmitter.models import Todolist
from dashboard.models import TblMDatabasesettings, Sessionmain

class TestModels(TestCase):
    
    def setUp(self):
        # Todolist 1
        self.Todolist = Todolist.objects.create(id = '01', eventtype = 'Triggered',eventid='01',todotypeid='01')

        # Sessionmain 2
        self.TestDataSessionmain= Sessionmain.objects.create(sessionmainid = '02', clientid = 'client02',clientcode='client02',sessionno='02')

        # TblMDatabasesettings 3
        self.TestDataTblMDatabasesettings= TblMDatabasesettings.objects.create(databasesettingsid = '03', 
        databasename = 'digicube',databasetype='tabuler',servername='express')
    
    def test_TblMDatabasesettings_models(self):
        objects = TblMDatabasesettings.objects.get(databasesettingsid='03')
        self.assertEqual(objects.databasesettingsid,'03')
        self.assertEqual(objects.databasename,'digicube')
        self.assertEqual(objects.databasetype,'tabuler')
        self.assertEqual(objects.servername,'express')


    def test_Sessionmain_models(self):
        objects = Sessionmain.objects.get(sessionmainid='02')
        self.assertEqual(objects.sessionmainid,'02')
        self.assertEqual(objects.clientid,'client02')
        self.assertEqual(objects.clientcode,'client02')
        self.assertEqual(objects.sessionno,'02')

    def test_Todolist_models(self):
        objects = Todolist.objects.get(id = '01')
        self.assertEqual(objects.id, '01')
        self.assertEqual(objects.eventtype, 'Triggered')
        self.assertEqual(objects.eventid, '01')
        self.assertEqual(objects.todotypeid, '01')