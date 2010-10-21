import auth
import config
import urllib
from lxml import etree

device_ids = None

def devices():
  global device_ids
  if device_ids != None: return device_ids
  xml = request("getDeviceList", userId = auth.user_id)
  device_list = xml_nodes(xml, "devList")
  device_ids = [device.findtext("devId") for device in device_list]
  return device_ids

def xml_value(xml, tag):
  dom = etree.fromstring(xml)
  return dom.findtext(tag)

def xml_nodes(xml, tag):
  dom = etree.fromstring(xml)
  return dom.findall(tag)

def request(request_name, **args):
  url = config.server + request_name + "?secToken=" + auth.token
  for arg in args:
    url += "&" + arg + "=" + args[arg]
  response = urllib.urlopen(url).read()
  return etree.tostring(etree.fromstring(response), pretty_print = True)
