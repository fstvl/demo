from common_files.read_configuration import read_config	
from common_files.jwt_token import make_jwt_token, extract_jwt_info, verify_jwt_token
from common_files.read_logger import get_logger
from common_files.create_response import create_failure_modified, create_success_modified, create_failure, create_success
from common_files.create_connection import db_conn

from django.core.serializers.json import DjangoJSONEncoder

import requests,json,csv,os,io,base64,hashlib,urllib
import pandas as pd
import datetime
from dateutil import parser
import time
import numpy as np


from dashboard.models import Excelimportmappingmain, ExcelImportMappingDetail
from sql_queries.upload_file_sql_query import upload_file_sql_query, upload_file_fetch_columns_sql_query
from .serializers import excelimportmappingmainSerializer, excelimportmappingdetailSerializer

########################################################################################################
# dump_file - is the main function. 
# parse_csv_file - is used to read csv file from the server and process it.
# parse_excel_file - is used to read excel file from the server and process it.
# insert_into_db - is used to run iteract with Database and execute pyodbc queries(insert)
# table_column_mapping - is used to map excel/csv file columns with the columns of database
# fetch_schema - is used to fetch datatypes of destination table, which is used while validating records and type conversion
# validate_record - is used for validation of records and converting data type of files w.r.t sql
########################################################################################################


logger = get_logger()
config = read_config()

def dump_file(request):
    try:
        fileType = request['FileType']
        if(fileType.lower() == "csv"):
            status,dataParse,tableSchema = parse_csv_file(request)
        elif(fileType.lower() == 'excel'):
            status,dataParse,tableSchema = parse_excel_file(request)
        if(status == True):
            dataUpdated = validate_record(request,dataParse,tableSchema)   
            if(dataUpdated is False):
                return create_failure(500, 'Data Type of Records is not valid', 'Failed')
            response = insert_into_db(request,dataUpdated)
            return response
    except Exception as e:
        logger.error("Error While Dumping File"+str(e))
        return create_failure(500, 'Error Wile Dumping File', 'Failed')
    return status

def parse_csv_file(request):
    try:
        filePath = request['FilePath']
    except Exception as e:
        logger.error("Error While Fetching File Path"+str(e))
        return create_failure(500, 'Error While Fetching File Path', 'Failed')
    try:
        textQual = request['textqualifier']
        if(len(textQual) == 0):
            textQual = ' '
    except Exception as e:
        logger.error("Error While Fetching TextQualifier "+str(e))
        return create_failure(500, 'Error While Fetching TextQualifier', 'Failed')
    try:
        rowDel = base64.b64decode(request['rowdelimeter']).decode("utf-8")
    except Exception as e:
        logger.error("Error While Fetching Row Delimeter"+str(e))
        return create_failure(500, 'Error While Fetching Row Delimeter', 'Failed')
    try:
        colDel = base64.b64decode(request['columndelimeter']).decode("utf-8")
    except Exception as e:
        logger.error("Error While Fetching Column Delimeter"+str(e))
        return create_failure(500, 'Error While Fetching Column Delimeter', 'Failed')
    try:
        noRowToSkip = int(request['numberRowToSkip'])
    except Exception as e:
        logger.error("Error While Fetching Number of Rows to Skip"+str(e))
        return create_failure(500, 'Error While Fetching Number of Rows to Skip', 'Failed')
    try:
        firstRowHeader = request['iscolumnnameinfirstrow']
        if(firstRowHeader == 'true'):
            firstRowHeader = 0
        else:
            firstRowHeader = None
    except Exception as e:
        logger.error("Error While Fetching Is ColumnName in First Row "+str(e))
        return create_failure(500, 'Error While Fetching Is ColumnName in First Row ', 'Failed')
    try:
        with open(filePath) as csv_data:
            data = csv_data.read()
        if(len(textQual) != 1):
            data = data.replace(textQual,"'")
            textQual = "'"
    except Exception as e:
        logger.error("Error While Processing CSV File "+str(e))
        return create_failure(500, 'Error While Processing CSV File', 'Failed')
    try:

        if(rowDel == '/r/n' or rowDel == '//r//n' or rowDel == '\\r\\n' or rowDel == '\r\n'):
            data = pd.read_csv(io.StringIO(data),encoding='ISO-8859-1',sep=colDel,header=firstRowHeader,skiprows=noRowToSkip,quotechar=textQual)
        elif(rowDel == '/n'):
            data = pd.read_csv(io.StringIO(data),encoding='ISO-8859-1',sep=colDel,lineterminator='\n',header=firstRowHeader,skiprows=noRowToSkip,quotechar=textQual)
        elif(rowDel == '/r'):
            data = pd.read_csv(io.StringIO(data),encoding='ISO-8859-1',sep=colDel,lineterminator='\r',header=firstRowHeader,skiprows=noRowToSkip,quotechar=textQual)
        else:
            data = pd.read_csv(io.StringIO(data),encoding='ISO-8859-1',sep=colDel,lineterminator=rowDel,header=firstRowHeader,skiprows=noRowToSkip,quotechar=textQual)
        data.replace({pd.NaT: None}, inplace=True)
        data.replace({pd.NA: None}, inplace=True)
        tableMapping = table_column_mapping(request)
        if(tableMapping is False):
            return create_failure(500, 'Error while Mapping File Columns to Table Columns', 'Failed')
        dataParse = data.rename(columns=tableMapping)
        tableSchema = fetch_schema(request,data)
        if(tableSchema is False):
            return create_failure(500, 'Error While Fetching Schema of table', 'Failed')
    except Exception as e:
        logger.error("Error While Processing CSV File "+str(e))
        return create_failure(500, 'Error While Processing CSV File', 'Failed')
    return (True,dataParse,tableSchema)

def parse_excel_file(request):
    try:
        filePath = request['FilePath']
        sheetName = request['SheetName']
    except Exception as e:
        logger.error("Error While Fetching Request Data"+str(e))
        return create_failure(500, 'Error While Fetching Request Data', 'Failed')
    try:
        data = pd.read_excel(open(filePath, 'rb'),sheet_name=sheetName)  
        data.replace({pd.NaT: None}, inplace=True)
        data.replace({pd.NA: None}, inplace=True)
        data.replace({np.nan: None}, inplace=True)
        tableMapping = table_column_mapping(request)
        if(tableMapping is False):
            return create_failure(500, 'Error while Mapping File Columns to Table Columns', 'Failed')
        dataParse = data.rename(columns=tableMapping)
        tableSchema = fetch_schema(request,data)
        if(tableSchema is False):
            return create_failure(500, 'Error While Fetching Schema of table', 'Failed')        
    except Exception as e:
        logger.error("Error While Processing Excel File "+str(e))
        return create_failure(500, 'Error While Processing Excel File', 'Failed')
    return (True,dataParse,tableSchema)

def insert_into_db(request,data):
    try:
        overwriteMerge = request['Overwrite_merge']
        databaseName = request['DatabaseName']
        tableName = request['TableName']
    except Exception as e:
        logger.error("Error While Inserting into Database"+str(e))
        return create_failure(500, 'Error While Inserting into Database', 'Failed')
    try:
        connection = db_conn(databaseName)
    except Exception as e:
        logger.error("Error While Creation of Engine "+str(e))
        return create_failure(500, 'Error While Creation of Engine', 'Failed')
    try:
        try:
            if(overwriteMerge == "O"):
                cursor = connection.cursor()
                cursor.execute('TRUNCATE TABLE {}'.format(tableName))
                connection.commit()
                cursor.close()
            elif(overwriteMerge != "M"):
                return False
        except Exception as e:
            logger.error("Error While Inserting into DB: "+str(e))
            return create_failure(500, 'Error While Inserting into DB ', 'Failed')
        cursor = connection.cursor()
        tuples = [tuple(x) for x in data.to_numpy()]
        cols = "],[".join([str(i) for i in data.columns.tolist()])
        databaseChunk = int(config['ENV_VARIABLE']['database_chunk'])
        chunk = int(len(tuples)/databaseChunk)
        cursor.fast_executemany = True
        for i in range(1,chunk+2):
            try:
                val = tuples[(i-1)*databaseChunk:i*databaseChunk]
                query = upload_file_sql_query(tableName,cols,data.columns)
                cursor.executemany(query,val)
            except Exception as e:
                cursor.close()
                connection.close()
                logger.error("Error While Inserting into DB "+str(e))
                return create_failure(500, 'Error While Inserting into DB', 'Failed')
        connection.commit()
        cursor.close()
        connection.close()
        logger.info("Success")
    except Exception as e:
        logger.error("Error While Inserting into DB "+str(e))
        return create_failure(500, 'Error While Inserting into DB', 'Failed')
    return(create_success('Data Dumped Successfully',''))

def table_column_mapping(request):
    try:
        clientId = request['ClientID']
        tableName = request['TableName']
        tableMapping = dict()
        excelImportMappingMainObject = Excelimportmappingmain.objects.filter(customercode=clientId, tablename = tableName)
        excelImportMappingMainData = excelimportmappingmainSerializer(excelImportMappingMainObject, many=True)
        if excelImportMappingMainObject.exists():
            try:
                for excelImportMappingMainRecord in excelImportMappingMainData.data:
                    try:
                        pid = excelImportMappingMainRecord['excelimportmappingmainid']
                        excelImportMappingDetailObject = ExcelImportMappingDetail.objects.filter(pid=pid)
                        excelImportMappingDetailData= excelimportmappingdetailSerializer(excelImportMappingDetailObject, many=True)
                        if excelImportMappingDetailObject.exists():
                            for mappingRecord in excelImportMappingDetailData.data:
                                tableMapping[mappingRecord['excelcolumncaption']] = mappingRecord['sqlcolumncaption']                  
                    except Exception as e:
                        logger.error("Error in ExcelImportMappingDetail: "+str(e))
                        return False
            except Exception as e:
                logger.error("Error in Excelimportmappingmain Table: "+str(e))
                return False
    except Exception as e:
        logger.error("Error in Fetching Data."+str(e))    
        return False
    return tableMapping

def fetch_schema(request,data):
    try:
        databaseName = request['DatabaseName']
        tableName = request['TableName']
    except Exception as e:
        logger.error("Error While Reteriving Payload"+str(e))
        return False
    try:
        connection = db_conn(databaseName)
        cursor = connection.cursor()
    except Exception as e:
        logger.error("Error While Creation of DB Connection "+str(e))
        return False
    try:
        query =  upload_file_fetch_columns_sql_query(tableName)
        queryResult = cursor.execute(query).fetchall()
        cursor.close()
        connection.close()
    except Exception as e:
        logger.error("Error While Performing Fetch Schema Operation"+str(e))
        return False
    return queryResult

def validate_record(request,data,tableSchema):
    try:
        correctCell = 0
        incorrectCell = 0
        tableSchemaUpdated = dict()
        dataUpdated = data.copy()
        columnDataTypeMap = {'varchar': str, 'nvarchar': str, 'float': float, 'int': int, 'date': str, 'datetime': str, 'numeric': float}
        for var in tableSchema:
            tableSchemaUpdated[var[0]] = var
        for i in tableSchemaUpdated:
            if((tableSchemaUpdated[i][2] == 'date' or tableSchemaUpdated[i][2] == 'datetime') and i in data.columns.tolist()):
                data[i] = data[i].astype(str)
        totalRows=len(data.axes[0])
        totalColumns=len(data.axes[1])
        for tableColumn in data.columns.tolist():
            try:
                for index,excelColumnValue in enumerate(data[tableColumn]):
                    try:
                        if(type(excelColumnValue) == columnDataTypeMap[tableSchemaUpdated[tableColumn][2]] or type(excelColumnValue) == type(None)):
                            correctCell = correctCell + 1
                        else:
                            if(incorrectCell > (totalRows*totalColumns)*0.05):
                                return False
                            incorrectCell = incorrectCell + 1
                            if(type(excelColumnValue) == pd._libs.tslibs.timestamps.Timestamp):
                                if(tableSchemaUpdated[tableColumn][2] == 'date'):
                                    dataUpdated.loc[index,tableColumn] = str(excelColumnValue)[:10]
                                else:    
                                    dataUpdated.loc[index,tableColumn] = str(excelColumnValue)
                            elif(columnDataTypeMap[tableSchemaUpdated[tableColumn][2]] == str):
                                dataUpdated.loc[index,tableColumn] = str(excelColumnValue)  
                            elif(columnDataTypeMap[tableSchemaUpdated[tableColumn][2]] == int):
                                dataUpdated.loc[index,tableColumn] = int(excelColumnValue)
                            elif(columnDataTypeMap[tableSchemaUpdated[tableColumn][2]] == float):
                                dataUpdated.loc[index,tableColumn] = float(excelColumnValue)
                    except Exception as e:
                        logger.error("Error While Validating Record: -"+str(e))
                        return False
            except Exception as e:
                logger.error("Error While Validating Record"+str(e))
                return False
    except Exception as e:
        logger.error("Error While Validating Record"+str(e))
        return False
    return dataUpdated
