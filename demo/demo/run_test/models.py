from django.db import models

# Create your models here.
class Storedproceduretable(models.Model):
    storedproceduretableid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ruledetailsid = models.CharField(db_column='RuleDetailsId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='ParamValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storedprocname = models.CharField(db_column='StoredProcName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'storedproceduretable'


class Pythonfunctionstable(models.Model):
    pythonfunctionsid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ruledetailsid = models.CharField(db_column='RuleDetailsId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='ParamValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pythonfunctionname = models.CharField(db_column='PythonFunctionName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    task_id = models.CharField(db_column='Task_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pythonfunctionstable'


class Sessiontestmapping(models.Model):
    sessiontestid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ruledetailsid = models.CharField(db_column='RuleDetailsID', max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=100)  # Field name made lowercase.
    todolistid = models.CharField(db_column='ToDoListID', max_length=50)  # Field name made lowercase.
    ruleid = models.CharField(db_column='RuleID', max_length=150)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    approvedon = models.DateTimeField(db_column='ApprovedOn', blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'SessionTestMapping'