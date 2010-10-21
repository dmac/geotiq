import user
import config
import urllib
from lxml import etree

DEV_ID = "3253"

def login(username, password):
  user.set_username(username)
  user.set_token(security_token(username, password))
  user.get_user_info()

def security_token(username, password):
  url = config.server + "userLogin?name=" + username + "&password=" + password + "&appId=" + config.app_id
  response = urllib.urlopen(url).read()
  dom = etree.fromstring(response)
  return dom.xpath("/ns1:userLoginResponse/securityToken", namespaces = config.namespaces)[0].text

def get_all_values():
  url = config.server + "getUserValueList?secToken=" + user.token() + "&userName=" + USERNAME
  response = urllib.urlopen(url).read()
  print response
  dom = etree.fromstring(response)
  valists = dom.xpath("/ns1:getUserValueListResponse/valist", namespaces = config.namespaces)
  names = [valist.xpath("name")[0].text for valist in valists]
  values = [valist.xpath("value")[0].text for valist in valists]
  return dict(zip(names, values))

def api_request(request_name, **args):
  url = config.server + request_name + "?secToken=" + user.token()
  for arg in args:
    url += "&" + arg + "=" + args[arg]
  response = urllib.urlopen(url).read()
  return etree.tostring(etree.fromstring(response), pretty_print = True)

# login("dan", "thebeast")
# print api_request("getDeviceValueList", deviceId=DEV_ID, type="2")


