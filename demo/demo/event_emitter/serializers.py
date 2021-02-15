from rest_framework import serializers
from .models import Todolist

class eventEmiiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todolist
        fields = '__all__'
