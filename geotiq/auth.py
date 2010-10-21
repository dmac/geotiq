import api
import config
import urllib

token = None
user_id = None

def login(username, password):
  global token
  global user_id
  token = security_token(username, password)
  user_id = user_id(username)

def security_token(username, password):
  url = config.server + "userLogin?name=" + username + "&password=" + password + "&appId=" + config.app_id
  xml = urllib.urlopen(url).read()
  return api.xml_value(xml, "securityToken")

def user_id(username):
  xml = api.request("getUserValueList", userName = username)
  return api.xml_value(xml, "userId")
