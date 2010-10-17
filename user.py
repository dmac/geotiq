import config
import api

_username = None
_token = None
_user_id = None

def get_user_info():
  global _user_id
  xml = api.request("getUserValueList", userName = _username)
  _user_id = api.xml_value(xml, "userId")

def user_id():
  return _user_id

def set_username(new_username):
  global _username
  _username = new_username

def username():
  return _username

def set_token(new_token):
  global _token
  _token = new_token

def token():
  if _token == None:
    raise Exception("No security token defined.  Have you called geotiq.auth.login?")
  else:
    return _token
