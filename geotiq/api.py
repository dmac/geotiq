import user
import config
import urllib
from lxml import etree

def devices():
  xml = request("getDeviceList", userId = user.user_id())
  return xml

def xml_value(xml, tag):
  dom = etree.fromstring(xml)
  return dom.findtext("userId")

def request(request_name, **args):
  url = config.server + request_name + "?secToken=" + user.token()
  for arg in args:
    url += "&" + arg + "=" + args[arg]
  response = urllib.urlopen(url).read()
  return etree.tostring(etree.fromstring(response), pretty_print = True)
