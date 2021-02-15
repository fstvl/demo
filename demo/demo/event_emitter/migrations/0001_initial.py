# Generated by Django 2.1.15 on 2020-09-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=50, primary_key=True, serialize=False)),
                ('eventtype', models.CharField(blank=True, db_column='EventType', max_length=50, null=True)),
                ('eventid', models.IntegerField(blank=True, db_column='EventID', null=True)),
                ('todotypeid', models.IntegerField(blank=True, db_column='ToDoTypeID', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('createdon', models.DateTimeField(blank=True, db_column='CreatedOn', null=True)),
                ('ruleid', models.CharField(blank=True, db_column='RuleID', max_length=50, null=True)),
                ('seqno', models.IntegerField(blank=True, db_column='SeqNo', null=True)),
                ('executedon', models.DateTimeField(blank=True, db_column='ExecutedOn', null=True)),
                ('nooftries', models.IntegerField(blank=True, db_column='NoOfTries', null=True)),
                ('sheet_name', models.CharField(blank=True, db_column='Sheet_Name', max_length=50, null=True)),
                ('failedreason', models.TextField(blank=True, db_column='FailedReason', null=True)),
                ('databaseformat', models.CharField(blank=True, db_column='DatabaseFormat', max_length=50, null=True)),
                ('auditfrom', models.DateTimeField(blank=True, db_column='AuditFrom', null=True)),
                ('auditto', models.DateTimeField(blank=True, db_column='AuditTo', null=True)),
                ('projectname', models.CharField(blank=True, db_column='ProjectName', max_length=150, null=True)),
                ('filepath', models.CharField(blank=True, db_column='FilePath', max_length=450, null=True)),
                ('tablename', models.CharField(blank=True, db_column='TableName', max_length=50, null=True)),
                ('filetype', models.CharField(blank=True, db_column='FileType', max_length=50, null=True)),
                ('clientid', models.CharField(blank=True, db_column='ClientID', max_length=50, null=True)),
                ('outputfolderpath', models.CharField(blank=True, db_column='OutputFolderPath', max_length=350, null=True)),
                ('outputfilename', models.TextField(blank=True, db_column='OutputFileName', null=True)),
                ('text_qualifier', models.CharField(blank=True, db_column='Text_qualifier', max_length=10, null=True)),
                ('header_row_delimiter', models.CharField(blank=True, db_column='Header_row_delimiter', max_length=10, null=True)),
                ('header_rows_to_skip', models.IntegerField(blank=True, db_column='Header_rows_to_skip', null=True)),
                ('row_delimiter', models.CharField(blank=True, db_column='Row_delimiter', max_length=10, null=True)),
                ('column_delimiter', models.CharField(blank=True, db_column='Column_delimiter', max_length=5, null=True)),
                ('overwrite_merge', models.CharField(blank=True, db_column='Overwrite_Merge', max_length=3, null=True)),
                ('sessionid', models.CharField(blank=True, db_column='SessionID', max_length=50, null=True)),
                ('outputpublishfolderpath', models.CharField(blank=True, db_column='OutputPublishFolderPath', max_length=500, null=True)),
                ('serialno', models.IntegerField(blank=True, db_column='SerialNo', null=True)),
            ],
            options={
                'db_table': 'TodoList',
            },
        ),
    ]