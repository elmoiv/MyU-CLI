import json, os
from .exceptions import IncorrectJsonException, JsonFilePathException

def get_credentials(json_path):
    if not os.path.exists(json_path):
        raise JsonFilePathException('Json path does not exist!')
    
    json_raw = open(json_path)
    dct = json.load(json_raw)
    
    if not 'username' in dct or not 'password' in dct:
        raise IncorrectJsonException('Username or Password keys not found in json!')
    
    return dct['username'], dct['password']