from django.test import TestCase
from eventEmitter.models import Todolist

class TestModels(TestCase):
    
    def set_up(self):
        # Todolist 1
        self.Todolist = Todolist.objects.create(id = '01', eventtype = 'Triggered',eventid='01',todotypeid='01')

    def test_Todolist_models(self):
        objects = Todolist.objects.get(id = '01')
        self.assertEqual(objects.id, '01')
        self.assertEqual(objects.eventtype, 'Triggered')
        self.assertEqual(objects.eventid, '01')
        self.assertEqual(objects.todotypeid, '01')