from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.request import HttpRequest, Request

from run_test import models
from dashboard.models import Ruledetails, Settings, Testparameter, Testparameterdetail

from common_files.read_logger import get_logger
from common_files.read_configuration import read_config
from common_files.create_connection import db_conn
from common_files.create_response import create_failure, create_success

import requests, datetime, json, zipfile, zlib, xlsxwriter, time, csv, os

def get_sp_payload(ruleDetailsId):
    try:
        payload = {}
        logger = get_logger()
        sptable = models.Storedproceduretable.objects.filter(ruledetailsid=ruleDetailsId).values_list('paramname',
                     'paramvalue')
        for sp in sptable:
            try:
                payload[sp[0]] = sp[1]
            except Exception as e:
                logger.error("Error in preparing payload for sp_query: ", str(e))
                return False
        logger.info("Payload for sp API: "+ str(payload))
    except Exception as e:
        logger.error("Error in preparing payload for sp_query: ", str(e))
        return False
    return payload

def sp_runtest(rule_id, ruleDetailsId) -> JsonResponse:
    try:
        logger = get_logger()
        connection = db_conn()
        payload = get_sp_payload(ruleDetailsId)
        if not payload:
            logger.error("Error in executing stored procedure ")
            return create_failure(500, 'Error in executing stored procedure', 'Failed')
        sptable = models.Storedproceduretable.objects.filter(ruledetailsid=ruleDetailsId).values_list('storedprocname')
        cursor = connection.cursor()
        for sp in sptable:
            try:
                logger.debug("exec digicube_wam.dbo.test_sp" + str(sp[0]))
                # resultset = cursor.execute("exec "+ str(sp[0])).fetchall()
                # if not resultset:
                #     return create_failure(500, 'Error in executing stored procedure', 'Failed')
            except Exception as e:
                logger.error("Error in executing stored procedure: ", str(e))
                return create_failure(500, 'Error in executing stored procedure', 'Failed')
        cursor.close()
        connection.close()
    except Exception as e:
        logger.error("Error in executing stored procedure: ", str(e))
        return create_failure(500, 'Error in executing stored procedure', 'Failed')
    return create_success('Success')

def get_api_parameter(ruleDetailsId):
    try:
        logger = get_logger()
        payload = {}
        pythonfunc = models.Pythonfunctionstable.objects.filter(ruledetailsid=ruleDetailsId).values_list('paramname',
                    'paramvalue')
        if pythonfunc.exists():
            for key,value in pythonfunc:
                payload[key] = value
        tmtable = Testparameter.objects.filter(ruledetailsid=ruleDetailsId).values_list('testparameterid',
                    'parametername', 'defaultvalue')
        if tmtable.exists():
            for tmitems in tmtable:
                try:
                    payload[tmitems[1]] = tmitems[2]
                    tmdetails = Testparameterdetail.objects.filter(ruledetailsid=ruleDetailsId, 
                        parameterid=tmitems[0]).values_list('value')
                    paramvalue = ''
                    for val in tmdetails:
                        for i in val:
                            paramvalue = i
                    # Replace default if value exists
                    if len(paramvalue) > 0:
                        payload[tmitems[1]] = paramvalue
                except Exception as e:
                    logger.error("Error in parsing ruledetails table: "+str(e))
                    return False
        if len(payload) == 0:
            return False
        logger.info("payload for API: "+ str(payload))
    except Exception as e:
        logger.error("Error in preparing payload for run test API: ", str(e))
        return False
    return payload

def api_run_test(rule_id, ruleDetailsId) -> JsonResponse:
    try:
        logger = get_logger()
        payload = get_api_parameter(ruleDetailsId)
        if not payload:
            logger.error("Error in run test API")
            return create_failure(500, 'Error in run test API', 'Failed')
        api_endpoint = ''
    except Exception as e:
        logger.error("Error in run test API: ", str(e))
        return create_failure(500, 'Error in run test API', 'Failed')
    return create_success('success')