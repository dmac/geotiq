import urllib
from lxml import etree

SERVER = "https://api.geotiq.com:8081/zdk/services/zamapi/"
GEOTIQ_APP_ID = "1004"
USERNAME = None
TOKEN = None
DEV_ID = "3253"

NAMESPACES = {
  "ns1": "http://arrayent.com/zamapi/",
}

def login(username, password):
  global USERNAME, TOKEN
  USERNAME = username
  TOKEN = security_token(username, password)

def security_token(username, password):
  url = SERVER + "userLogin?name=" + username + "&password=" + password + "&appId=" + GEOTIQ_APP_ID
  response = urllib.urlopen(url).read()
  dom = etree.fromstring(response)
  return dom.xpath("/ns1:userLoginResponse/securityToken", namespaces = NAMESPACES)[0].text

def get_all_values():
  global TOKEN
  url = SERVER + "getUserValueList?secToken=" + TOKEN + "&userName=" + USERNAME
  response = urllib.urlopen(url).read()
  print response
  dom = etree.fromstring(response)
  valists = dom.xpath("/ns1:getUserValueListResponse/valist", namespaces = NAMESPACES)
  names = [valist.xpath("name")[0].text for valist in valists]
  values = [valist.xpath("value")[0].text for valist in valists]
  return dict(zip(names, values))

def api_request(request_name, **args):
  global TOKEN
  url = SERVER + request_name + "?secToken=" + TOKEN
  for arg in args:
    url += "&" + arg + "=" + args[arg]
  response = urllib.urlopen(url).read()
  return etree.tostring(etree.fromstring(response), pretty_print = True)

login("dan", "thebeast")
print api_request("getDeviceValueList", deviceId=DEV_ID, type="2")


