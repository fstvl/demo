def insert_record_in_tbl_m_database_table(databasesettingsid,databasename,databasetype,servername,username,iswinauthentication,publisheddatetime,password):
    query = "INSERT INTO tbl_m_DatabaseSettings (ID,DatabaseName, DatabaseType, ServerName, UserName, IsWinAuthentication, PublishedDateTime, Password) VALUES ('"+databasesettingsid+"','"+databasename+"','"+databasetype+"','"+servername+"','"+username+"','"+iswinauthentication+"','"+publisheddatetime+"',"+"CONVERT(VARBINARY(300), '"+password+"')"+")"
    return query