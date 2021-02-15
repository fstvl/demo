from django.http.response import JsonResponse
from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
import pyodbc
config = read_config()
logger = get_logger()


def db_conn(database = config['DIGICUBEDB']['database_name']):
    output = {
        'statusCode':400,
        'message': 'Error in db connection',
        'replyCode': 'Fail',
        'data': {}
    }
    try:
        driver = config['DIGICUBEDB']['driver']
        server = config['DIGICUBEDB']['server']
        uid = config['DIGICUBEDB']['username']
        password = config['DIGICUBEDB']['password']
        connection = pyodbc.connect("driver={};server={};database={};uid={};PWD={}".format(driver, server, database, uid, password),autocommit=False)
        return connection
    except Exception as e:
        logger.error("Error in db connection: "+str(e))
        return JsonResponse(output)
