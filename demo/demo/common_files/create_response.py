from django.http.response import JsonResponse

def create_failure(statusCode, message, replyCode):
    output = {
        'statusCode' : statusCode,
        'message' : message,
        'replyCode' : replyCode
        }
    return output

def create_success(message, data = {}):
    output = {
        'statusCode' : 200,
        'message' : message,
        'replyCode' : 'Success',
        'data' : data
    }
    return output

def create_failure_modified(statusCode, message, replyCode, data = {}, status = {}):
    output = {
        'statusCode' : statusCode,
        'message' : message,
        'replyCode' : replyCode,
        'data' : data,
        'status' : status
    }
    return output

def create_success_modified(message, data = {}, status = {}):
    output = {
        'statusCode' : 200,
        'message' : message,
        'replyCode' : 'Success',
        'data' : data,
        'status': status
    }
    return output