import jwt
from common_files.read_logger import get_logger
from common_files.read_configuration import read_config


def extract_jwt_info(token: str) -> dict:
    """
    This function decode jwt token which we will receive from UI
    :param token: this is string type of input which contains jwt token.
        Sample token:
        eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0
    :return:
    """
    logger = get_logger()
    config = read_config()
    json_info = dict()
    try:
        jwt_secret_key = config['JWT']['jwt_secret_key']
        jwt_algo = config['JWT']['jwt_algo']
        json_info = jwt.decode(str(token), jwt_secret_key, algorithms=str(jwt_algo))
    except Exception as e:
        logger.error(str(e))
    return json_info


def make_jwt_token(data: dict) -> str:
    """
    This function encode jwt token
    :param token: this is string type of input which contains jwt token.
        Sample token:
        eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJVLTEifQ.aRzeeoMrtxJIi9HB4_9YoVnzJ16tgM0Xux5_q6q0gh0
    :return:
    """
    logger = get_logger()
    config = read_config()
    token = str()
    try:
        jwt_secret_key = config['JWT']['jwt_secret_key']
        jwt_algo = config['JWT']['jwt_algo']
        token = jwt.encode(data, jwt_secret_key, jwt_algo).decode('utf-8')
    except Exception as e:
        token = str()
        logger.error(str(e))
    return token

def verify_jwt_token(token: str) -> dict:
    userid_dict = extract_jwt_info(token)
    try:
        userid = userid_dict['userid']
        encode_userid = make_jwt_token(data={'userid':userid})
        if str(token) == encode_userid:
            return userid
        else:
            return 0
    except Exception as e:
        return 0
