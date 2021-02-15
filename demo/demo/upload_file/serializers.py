from rest_framework import serializers
from dashboard.models import TblMDatabasesettings, Sessionmain, Excelimportmappingmain, ExcelImportMappingDetail

class sessionmainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessionmain
        fields = '__all__'

class tblmdatabasesettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblMDatabasesettings
        fields = '__all__'

class excelimportmappingmainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Excelimportmappingmain
        fields = '__all__'

class excelimportmappingdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcelImportMappingDetail
        fields = '__all__'
