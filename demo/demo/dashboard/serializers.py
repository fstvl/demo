from rest_framework import serializers
from .models import Settings, Sectormaster, Usertosectormapping, Testparameter,Testparameterdetail, Excelimportmappingmain, Riskcontrol, Riskdetail, Riskmaster

class settingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ['label1', 'label2', 'label3', 'layercount', 'numberoffilesrequiredforzip', 'settingsid']

class sectormasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sectormaster
        fields = '__all__'

class usertosectormappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usertosectormapping
        fields = 'usertosectorid'

class testparameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testparameter
        fields = ['testparameterid','ruledetailsid','parametername','parameterdatatype','edittypecontrol','defaultvalue','caption',
            'createdby','createddate','modifiedby','modifieddate','exeversionno','modulename','enteredonmachineid','sysmodifieddatetime',
            'publisheddatetime','sessiondetailid']

class TestparameterdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testparameterdetail
        fields = ['parameterid','createddate','value','sessionid','sessiondetailid','testparameterdetailsid']

class ExcelimportmappingmainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Excelimportmappingmain
        fields = '__all__'


class RiskMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Riskmaster
        fields = '__all__'

class RiskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Riskdetail
        fields = '__all__'

class RiskControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Riskcontrol
        fields = '__all__'


