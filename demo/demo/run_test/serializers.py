from rest_framework import serializers
from event_emitter.models import Todolist
from dashboard.models import Ruledetails, Settings

class todolistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todolist
        fields = '__all__'

class settingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = '__all__'


class ruledetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ruledetails
        fields = '__all__'
