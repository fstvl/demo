# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Todolist(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID', blank=True, null=True)  # Field name made lowercase.
    todotypeid = models.IntegerField(db_column='ToDoTypeID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    ruleid = models.CharField(db_column='RuleID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    executedon = models.DateTimeField(db_column='ExecutedOn', blank=True, null=True)  # Field name made lowercase.
    nooftries = models.IntegerField(db_column='NoOfTries', blank=True, null=True)  # Field name made lowercase.
    sheet_name = models.CharField(db_column='Sheet_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    failedreason = models.TextField(db_column='FailedReason', blank=True, null=True)  # Field name made lowercase.
    databaseformat = models.CharField(db_column='DatabaseFormat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    auditfrom = models.DateTimeField(db_column='AuditFrom', blank=True, null=True)  # Field name made lowercase.
    auditto = models.DateTimeField(db_column='AuditTo', blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=450, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    outputfolderpath = models.CharField(db_column='OutputFolderPath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    outputfilename = models.TextField(db_column='OutputFileName', blank=True, null=True)  # Field name made lowercase.
    text_qualifier = models.CharField(db_column='Text_qualifier', max_length=10, blank=True, null=True)  # Field name made lowercase.
    header_row_delimiter = models.CharField(db_column='Header_row_delimiter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    header_rows_to_skip = models.IntegerField(db_column='Header_rows_to_skip', blank=True, null=True)  # Field name made lowercase.
    row_delimiter = models.CharField(db_column='Row_delimiter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_delimiter = models.CharField(db_column='Column_delimiter', max_length=5, blank=True, null=True)  # Field name made lowercase.
    overwrite_merge = models.CharField(db_column='Overwrite_Merge', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    outputpublishfolderpath = models.CharField(db_column='OutputPublishFolderPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TodoList'

