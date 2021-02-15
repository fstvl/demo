def upload_file_sql_query(tableName,cols,dataColumns):
    query = "INSERT INTO ["+tableName+"] ([" +cols + "]) values(" + "?,"*(len(dataColumns)-1) + "?)"
    return query

def upload_file_fetch_columns_sql_query(tableName):
    query = """SELECT sysColumn.name,sysColumn.max_length,sysType.name 
                  FROM sys.columns as sysColumn 
                  JOIN sys.types as sysType 
                  ON sysColumn.user_type_id = sysType.user_type_id 
                  WHERE sysColumn.object_id = Object_id('{}')""".format(tableName)
    return query              