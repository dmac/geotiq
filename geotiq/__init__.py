import api
import auth

def login(username, password):
  auth.login(username, password)

def devices():
  return api.devices()

def device_status(device_id):
  xml = api.request("getDevicePresenceInfo", devId = device_id)
  return api.xml_value(xml, "state")

def device_attributes(device_id):
  xml = api.request("getDeviceValueList", deviceId = device_id, type = "2")
  valists = api.xml_nodes(xml, "valist")
  attributes = {}
  for valist in valists:
    attributes[valist.findtext("name")] = valist.findtext("value")
  return attributes

def device_attribute(device_id, attribute, value = None):
  if value:
    xml = api.request("setDeviceAttribute", devId = device_id, name = attribute, value = value)
    return api.xml_value(xml, "retCode") == "0"
  else:
    xml = api.request("getDeviceAttribute", devId = device_id, name = attribute)
    return api.xml_value(xml, "value")
