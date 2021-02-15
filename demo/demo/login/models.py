from django.db import models


class Userlogindetails(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.BinaryField(db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    landlineno = models.CharField(db_column='LandLineNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100,unique=True, blank=False, null=False)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    enteredonmachineid = models.CharField(db_column='EnteredOnMachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exeversionno = models.CharField(db_column='ExeVersionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvedon = models.DateTimeField(db_column='ApprovedOn', blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    salutation = models.CharField(db_column='Salutation', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mbsn = models.BinaryField(db_column='MBSN', blank=True, null=True)  # Field name made lowercase.
    sysmodifieddatetime = models.DateTimeField(db_column='SysModifiedDateTime', blank=True, null=True)  # Field name made lowercase.
    publisheddatetime = models.DateTimeField(db_column='PublishedDateTime', blank=True, null=True)  # Field name made lowercase.
    isinternaluser = models.BooleanField(db_column='IsInternalUser', blank=True, null=True)  # Field name made lowercase.
    isruleeditable = models.BooleanField(db_column='IsRuleEditable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserLoginDetails'