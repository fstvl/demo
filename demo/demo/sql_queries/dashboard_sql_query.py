def get_table_data_for_date_range_sql(db_name, table_name, start_date, end_date, column_name):
    query = "select count(*) from ["+str(db_name)+"].[dbo].["+str(table_name)+"]"\
        " where cast(["+str(column_name)+"] as date) >= '"+str(start_date)+"' and cast(["+str(column_name)+"] as date)"\
        " <= '"+str(end_date)+"'"
    return query

def get_fetch_table_details(dbName, riskId, subproccessID, ruleId):
    if(len(riskId) == 1):
        riskId =  "('" + riskId[0] + "')"
    if(len(subproccessID) == 1):
        subproccessID =  "('" + subproccessID[0] + "')"
    if(len(ruleId) == 1):
        ruleId =  "('" + ruleId[0] + "')"
    
    query = """SELECT SeqNo, TableCaption, 'Pending' as UploadStatus, 'none' as FileType, TABLE_NAME as TableName, COLUMN_NAME as ColumnName, 
            DATA_TYPE as DataType, CHARACTER_MAXIMUM_LENGTH as CharacterMaximumLength, counts as Counts, ISNULL(MDC.SQLColumnCaption, 0) as IsRequired, ModifiedDate, B.AutomatedManual, B.DefaultColumnOnDateRangeFilter, B.HasDateRangeFilter
            FROM [{0}].INFORMATION_SCHEMA.COLUMNS as A
            inner join 
            ( 
                SELECT DISTINCT isnull(SeqNo,1) as SeqNo, TableName, TableCaption, AutomatedManual, DefaultColumnOnDateRangeFilter, HasDateRangeFilter
                from [ey_digicube].[dbo].[RuleTableRequirement] as RTR
                inner join (SELECT * FROM [ey_digicube].[dbo].[RuleMaster]) as RuleM
                on RuleM.ID = RTR.RuleID
                inner join (SELECT * FROM [ey_digicube].[dbo].[RiskMaster]) as RiskM
                on RiskM.ID = RuleM.RiskID WHERE RiskM.ID in {1} AND RuleM.ProcessID in {2} AND RTR.RuleID in {3} 
            ) B
            on A.TABLE_NAME=B.TableName COLLATE DATABASE_DEFAULT
            inner join 
            (
                SELECT T.NAME COLLATE DATABASE_DEFAULT as 'T_name', P.[ROWS] as counts
                FROM [{0}].SYS.TABLES T INNER JOIN [{0}].SYS.PARTITIONS P ON T.OBJECT_ID=P.OBJECT_ID 
            ) c
            on b.TableName = c.T_name
            LEFT JOIN MandatoryColumns as MDC
            on TABLE_NAME COLLATE DATABASE_DEFAULT =  MDC.TableName COLLATE DATABASE_DEFAULT and 
            COLUMN_NAME = MDC.SQLColumnCaption COLLATE DATABASE_DEFAULT""".format(dbName, riskId, subproccessID, ruleId)

    return query

def get_sql_query_fetch_tests(databaseName,riskId):
    if(len(riskId) == 1):
        riskId =  "('" + riskId[0] + "')"
    sqlQuery = """select RM.ID, TestNo, (CASE WHEN RM.PID='-1' THEN RM.TestName
             ELSE RM.DetailedDescription END ) AS TestName, RM.DetailedDescription
            , RM.ShortDescription, RM.ProcessID, RM.PID, RM.SubProcessName,
             RTR.TableName, RES.counts, RiD.RiskL1Name, RiD.RiskL2Name, RiD.id as RiskId, rim.TestNumber,
             RM.ID as RuleID from RuleMaster RM left join RuleTableRequirement RTR
             on RTR.RuleID=RM.ID left join (SELECT T.NAME COLLATE
            Latin1_General_CI_AI as 'T_name', P.[ROWS] as counts
            FROM [{0}].SYS.TABLES T INNER JOIN [{0}].SYS.PARTITIONS P ON
            T.OBJECT_ID=P.OBJECT_ID) res on res.T_name=RTR.TableName left join
            RuleDetails RD on RD.RuleID = RTR.RuleID left join RiskMaster rim
            on rim.ID = RM.RiskID join [RiskDetail] RiD on rim.RiskDetailID = RiD.ID  where RM.ProcessID = rim.ProcessID  and rim.ID in {1}""".format(databaseName,riskId)
    return sqlQuery
