from django.db import models

class Settings(models.Model):
    settingsid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    wsurl = models.CharField(db_column='WSUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    exeupdateurl = models.CharField(db_column='ExeUpdateURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    outputrootdirectory = models.CharField(db_column='OutputRootDirectory', max_length=350, blank=True, null=True)  # Field name made lowercase.
    powerbioutputrootdirectory = models.CharField(db_column='PowerBIOutputRootDirectory', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fileextension = models.CharField(db_column='FileExtension', max_length=4, blank=True, null=True)  # Field name made lowercase.
    columndelimiter = models.CharField(db_column='ColumnDelimiter', max_length=4, blank=True, null=True)  # Field name made lowercase.
    label1 = models.CharField(db_column='Label1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    label2 = models.CharField(db_column='Label2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    label3 = models.CharField(db_column='Label3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberoffilesrequiredforzip = models.IntegerField(db_column='NumberOfFilesRequiredForZip', blank=True, null=True)  # Field name made lowercase.
    appurl = models.CharField(db_column='AppURL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    publishedfolder = models.CharField(db_column='PublishedFolder', max_length=500, blank=True, null=True)  # Field name made lowercase.
    layercount = models.IntegerField(db_column='LayerCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Settings'


class Usertosettingsmapping(models.Model):
    usertosettingsid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    settingsid = models.CharField(db_column='SettingsID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserToSettingsMapping'


class Sectormaster(models.Model):
    sectormasterid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lefticonimagename = models.CharField(db_column='LeftIconImageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lefticonlablecaption = models.CharField(db_column='LeftIconLableCaption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    landingpagegif = models.CharField(db_column='LandingPageGIF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    testresultprefix = models.CharField(db_column='TestResultPrefix', max_length=5, blank=True, null=True)  # Field name made lowercase.
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
    blankdbbackupname = models.CharField(db_column='BlankDBBackupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blankdblogicalname = models.CharField(db_column='BlankDBLogicalName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blankdbname = models.CharField(db_column='BlankDBName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blankdbbackup_path = models.CharField(db_column='BlankDBBackup_Path', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fileextension = models.CharField(db_column='FileExtension', max_length=4, blank=True, null=True)  # Field name made lowercase.
    columndelimiter = models.CharField(db_column='ColumnDelimiter', max_length=5, blank=True, null=True)  # Field name made lowercase.
    databaseformat = models.CharField(db_column='DatabaseFormat', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'SectorMaster'


class Usertosectormapping(models.Model):
    usertosectorid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sectorid = models.CharField(db_column='SectorID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserToSectorMapping'


class Clientmaster(models.Model):
    clientmasterid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clientcode = models.CharField(db_column='ClientCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    engagementcode = models.CharField(db_column='EngagementCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iftestsarebyrisk = models.BooleanField(db_column='IfTestsAreByRisk', blank=True, null=True)  # Field name made lowercase.
    allowcreatenewsession = models.BooleanField(db_column='AllowCreateNewSession', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClientMaster'


class Usertoclientmapping(models.Model):
    userclientmappingid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserToClientMapping'


class Clienttoprocessmapping(models.Model):
    clientprocessmappingid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processid = models.CharField(db_column='ProcessID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClientToProcessMapping'


class Processmaster(models.Model):
    processmasterid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    processname = models.CharField(db_column='ProcessName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subprocessname = models.TextField(db_column='SubProcessName', blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(db_column='PID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processdescription = models.CharField(db_column='ProcessDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    subtitle = models.CharField(db_column='SubTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequenceno = models.IntegerField(db_column='SequenceNo', blank=True, null=True)  # Field name made lowercase.
    testno = models.DecimalField(db_column='TestNo', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'ProcessMaster'


class Sessionmain(models.Model):
    sessionmainid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clientcode = models.CharField(db_column='ClientCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionno = models.CharField(db_column='SessionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbid = models.CharField(db_column='DBID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionstartdate = models.DateTimeField(db_column='SessionStartDate', blank=True, null=True)  # Field name made lowercase.
    sessionenddate = models.DateTimeField(db_column='SessionEndDate', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    auditfrom = models.DateTimeField(db_column='AuditFrom', blank=True, null=True)  # Field name made lowercase.
    auditto = models.DateTimeField(db_column='AuditTo', blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        db_table = 'SessionMain'


class TblMDatabasesettings(models.Model):
    databasesettingsid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    databasetype = models.CharField(db_column='DatabaseType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iswinauthentication = models.BooleanField(db_column='IsWinAuthentication', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tbl_m_DatabaseSettings'

 
class Rulemaster(models.Model):
    rulemasterid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    subprocessname = models.TextField(db_column='SubProcessName', blank=True, null=True)  # Field name made lowercase.
    testno = models.CharField(db_column='TestNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    testname = models.TextField(db_column='TestName', blank=True, null=True)  # Field name made lowercase.
    detaileddescription = models.TextField(db_column='DetailedDescription', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='ShortDescription', blank=True, null=True)  # Field name made lowercase.
    takenoteon = models.TextField(db_column='TakeNoteOn', blank=True, null=True)  # Field name made lowercase.
    includeinstats = models.BooleanField(db_column='IncludeInStats', blank=True, null=True)  # Field name made lowercase.
    processname = models.TextField(db_column='ProcessName', blank=True, null=True)  # Field name made lowercase.
    processid = models.CharField(db_column='ProcessID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pivottableid = models.CharField(db_column='PivotTableID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(db_column='PID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    riskid = models.CharField(db_column='RiskID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'RuleMaster'


class Clienttosubprocessmapping(models.Model):
    clientsubprocessmappingid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subprocessid = models.CharField(db_column='SubProcessID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClientToSubProcessMapping'


class Testparameter(models.Model):
    testparameterid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ruledetailsid = models.CharField(db_column='RuleDetailsID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametername = models.CharField(db_column='ParameterName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parameterdatatype = models.CharField(db_column='ParameterDataType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edittypecontrol = models.CharField(db_column='EditTypeControl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=400, blank=True, null=True)  # Field name made lowercase.
    captionleft = models.IntegerField(db_column='CaptionLeft', blank=True, null=True)  # Field name made lowercase.
    captiontop = models.IntegerField(db_column='CaptionTop', blank=True, null=True)  # Field name made lowercase.
    captionheight = models.IntegerField(db_column='CaptionHeight', blank=True, null=True)  # Field name made lowercase.
    captionwidth = models.IntegerField(db_column='CaptionWidth', blank=True, null=True)  # Field name made lowercase.
    captionforecolor = models.IntegerField(db_column='CaptionForeColor', blank=True, null=True)  # Field name made lowercase.
    captionbackcolor = models.IntegerField(db_column='CaptionBackColor', blank=True, null=True)  # Field name made lowercase.
    valueleft = models.IntegerField(db_column='ValueLeft', blank=True, null=True)  # Field name made lowercase.
    valuetop = models.IntegerField(db_column='ValueTop', blank=True, null=True)  # Field name made lowercase.
    valueheight = models.IntegerField(db_column='ValueHeight', blank=True, null=True)  # Field name made lowercase.
    valuewidth = models.IntegerField(db_column='ValueWidth', blank=True, null=True)  # Field name made lowercase.
    valueforecolor = models.IntegerField(db_column='ValueForeColor', blank=True, null=True)  # Field name made lowercase.
    valuebackcolor = models.IntegerField(db_column='ValueBackColor', blank=True, null=True)  # Field name made lowercase.
    captionhalignment = models.CharField(db_column='CaptionHAlignment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    captionvalignment = models.CharField(db_column='CaptionVAlignment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valuehalignment = models.CharField(db_column='ValueHAlignment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valuevalignment = models.CharField(db_column='ValueVAlignment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fontname = models.CharField(db_column='FontName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize', blank=True, null=True)  # Field name made lowercase.
    isbold = models.BooleanField(db_column='IsBold')  # Field name made lowercase.
    isitalic = models.BooleanField(db_column='IsItalic')  # Field name made lowercase.
    isunderline = models.BooleanField(db_column='IsUnderline')  # Field name made lowercase.
    isstrikeout = models.BooleanField(db_column='IsStrikeOut')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    sessiondetailid = models.CharField(db_column='SessionDetailID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TestParameter'


class Ruledetails(models.Model):
    ruledetailsid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ruleid = models.CharField(db_column='RuleID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequenceno = models.IntegerField(db_column='SequenceNo', blank=True, null=True)  # Field name made lowercase.
    subprocesscaption = models.TextField(db_column='SubProcessCaption', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='ShortDescription', blank=True, null=True)  # Field name made lowercase.
    ruletype = models.CharField(db_column='RuleType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resulttablename = models.CharField(db_column='ResultTableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resultquery = models.TextField(db_column='ResultQuery', blank=True, null=True)  # Field name made lowercase.
    resultorderbycols = models.TextField(db_column='ResultOrderByCols', blank=True, null=True)  # Field name made lowercase.
    outputtemplate = models.CharField(db_column='OutputTemplate', max_length=150, blank=True, null=True)  # Field name made lowercase.
    worksheetname = models.TextField(db_column='WorkSheetName', blank=True, null=True)  # Field name made lowercase.
    ispowerbioutputrequired = models.BooleanField(db_column='IsPowerBIOutputRequired', blank=True, null=True)  # Field name made lowercase.
    isannexureoutputrequired = models.BooleanField(db_column='IsAnnexureOutputRequired', blank=True, null=True)  # Field name made lowercase.
    isvisibleondashboard = models.BooleanField(db_column='IsVisibleOnDashboard', blank=True, null=True)  # Field name made lowercase.
    dashboardcaption = models.TextField(db_column='DashboardCaption', blank=True, null=True)  # Field name made lowercase.
    dashboardseqno = models.CharField(db_column='DashboardSeqNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dashboardtestno = models.CharField(db_column='DashboardTestNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isdefined = models.BooleanField(db_column='IsDefined', blank=True, null=True)  # Field name made lowercase.
    showwaitdialog = models.BooleanField(db_column='ShowWaitDialog', blank=True, null=True)  # Field name made lowercase.
    variance = models.CharField(db_column='Variance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aggregatefunction = models.CharField(db_column='AggregateFunction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=500, blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    isoutputrequired = models.BooleanField(blank=True, null=True)
    annexurefilename = models.CharField(db_column='AnnexureFileName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    requiresqlrestart = models.BooleanField(db_column='RequireSQLRestart', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'RuleDetails'


class Testparameterdetail(models.Model):
    testparameterdetailid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    parameterid = models.CharField(db_column='ParameterID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ruledetailsid = models.CharField(db_column='RuleDetailsID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    sessiondetailid = models.CharField(db_column='SessionDetailID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TestParameterDetail'

class ExcelImportMappingDetail(models.Model):
    excelimportmappingdetailid =  models.CharField( db_column = 'ID', primary_key=True, max_length =50)
    excelcolumncaption = models.CharField( db_column = 'ExcelColumnCaption', max_length =500,blank=True, null=True)
    sqlcolumncaption = models.CharField( db_column = 'SQLColumnCaption', max_length = 500,blank=True, null=True)
    pid = models.CharField( db_column = 'PID', max_length = 50,blank=True, null=True)
    createdby = models.CharField( db_column = 'CreatedBy', max_length = 100,blank=True, null=True)
    createddate = models.DateTimeField( db_column = 'CreatedDate',blank=True, null=True)
    modifiedby = models.CharField( db_column = 'ModifiedBy', max_length =100,blank=True, null=True )
    modifieddate = models.DateTimeField( db_column = 'ModifiedDate',blank=True, null=True)
    exeversionno = models.CharField( db_column = 'ExeVersionNo', max_length = 50,blank=True, null=True)
    modulename = models.CharField( db_column = 'ModuleName', max_length = 100,blank=True, null=True)
    enterdonmachineid = models.CharField( db_column = 'EnteredOnMachineID', max_length = 50,blank=True, null=True)
    tablename = models.CharField( db_column = 'TableName', max_length = 500,blank=True, null=True)
    customercode = models.CharField( db_column = 'CustomerCode', max_length = 50,blank=True, null=True)
    isactive = models.BooleanField( db_column = 'IsActive',blank=True, null=True)
    sysmodifieddatetime = models.DateTimeField( db_column = 'SysModifiedDateTime',blank=True, null=True)
    publisheddatetime = models.DateTimeField( db_column = 'PublishedDateTime',blank=True, null=True)

    class Meta:
        db_table = 'ExcelImportMappingDetail'


class SessionDetail(models.Model):
    sessiondetailid = models.CharField(db_column='ID',primary_key=True, max_length = 500)
    sessionid = models.CharField(db_column='SessionID', max_length = 500, blank = True, null = True)
    testno = models.CharField(db_column='TestNo', max_length = 500, blank = True, null = True)
    ruledetailsid = models.CharField(db_column='RuleDetailsID', max_length = 500, blank = True, null = True)
    ruletype = models.CharField(db_column='RuleType', max_length = 500, blank = True, null = True)
    status = models.CharField(db_column='Status', max_length = 500, blank = True, null = True)
    totalrecords = models.IntegerField(db_column='TotalRecords', blank = True, null = True)
    failedrecords = models.IntegerField(db_column='FailedRecords', blank = True, null = True)
    testremarks = models.CharField(db_column='TestRemarks', max_length = 500, blank = True, null = True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank = True, null = True)
    createdby = models.CharField(db_column='CreatedBy', max_length = 500, blank = True, null = True)
    modifiedby = models.CharField(db_column='ModifiedBy', max_length = 500, blank = True, null = True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank = True, null = True)
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length = 500, blank = True, null = True)
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length = 500, blank = True, null = True)
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank = True, null = True)
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime',blank = True, null = True)
    testperameter = models.CharField(db_column='TestParameter', max_length = 500, blank = True, null = True)
    
    class Meta:
        db_table = 'SessionDetail'

class Excelimportmappingmain(models.Model):
    excelimportmappingmainid = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ExcelImportMappingMain'

class TestClientTemplateMapping(models.Model):
    testclienttemplatemappingid = models.CharField(db_column='ID', primary_key=True, max_length = 255)
    clientid = models.CharField(db_column='ClientID', max_length = 50, blank = True, null=True)
    testno = models.CharField(db_column='TestNo', max_length = 50, blank = True, null=True)
    dashboardtype = models.CharField(db_column='DashboardType', max_length = 50, blank = True, null=True)
    templatefilename = models.CharField(db_column='TemplateFileName', max_length = 100, blank = True, null=True)
    templatesourcefilename = models.CharField(db_column='TemplateSourceFileName', max_length = 500, blank = True, null=True)
    createdby = models.CharField(db_column='CreatedBy', max_length = 100 , blank = True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank = True, null=True)
    modifiedby = models.CharField(db_column='ModifiedBy', max_length = 100, blank = True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank = True, null=True)
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length = 50, blank = True, null=True)
    modulename = models.CharField(db_column='ModuleName', max_length = 100, blank = True, null=True)
    enterdonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length = 50, blank = True, null=True)
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank = True, null=True)
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank = True, null=True)
    sector = models.CharField(db_column='Sector', max_length = 500, blank = True, null=True)
    ruleid = models.CharField(db_column='RuleID', max_length = 500, blank = True, null=True)
    url = models.CharField(db_column='URL',max_length = 4000, blank = True, null=True)

    class Meta:
        db_table = 'Test_Client_TemplateMapping'

class Riskcontrol(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    riskl2id = models.CharField(db_column='RiskL2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    controlname = models.CharField(db_column='ControlName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    controldescription = models.CharField(db_column='ControlDescription', max_length=150, blank=True, null=True)  # Field name made lowercase.
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
        managed = False
        db_table = 'RiskControl'


class Riskdetail(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    riskl1id = models.CharField(db_column='RiskL1ID', max_length=50)  # Field name made lowercase.
    riskl1name = models.CharField(db_column='RiskL1Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    riskl1description = models.CharField(db_column='RiskL1Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    riskl2id = models.CharField(db_column='RiskL2ID', max_length=50)  # Field name made lowercase.
    riskl2name = models.CharField(db_column='RiskL2Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    riskl2description = models.CharField(db_column='RiskL2Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
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
        managed = False
        db_table = 'RiskDetail'


class Riskmaster(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    processid = models.CharField(db_column='ProcessID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    risk = models.CharField(db_column='Risk', max_length=100, blank=True, null=True)  # Field name made lowercase.
    riskdetails = models.CharField(db_column='RiskDetails', max_length=150, blank=True, null=True)  # Field name made lowercase.
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
    testnumber = models.CharField(db_column='TestNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    riskdetailid = models.CharField(db_column='RiskDetailID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiskMaster'
