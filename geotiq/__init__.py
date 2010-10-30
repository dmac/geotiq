import api
import auth
import urllib

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
  if value != None:
    xml = api.request("setDeviceAttribute", devId = device_id, name = attribute, value = str(value))
    return api.xml_value(xml, "retCode") == "0"
  else:
    xml = api.request("getDeviceAttribute", devId = device_id, name = attribute)
    return api.xml_value(xml, "value")

def alerts(device_id):
  xml = api.request("getTriggerList", devId = device_id)
  return api.xml_node_values(xml, "triggerList")

def add_alert(device_id, action, attr_name, operation, threshold, address, msg):
  if action != "email" and action != "twitter":
    raise Exception("Error: action must be one of \"email\" or \"twitter\"")
  xml = api.request("addTrigger", devId = device_id, action = action,
      attrName = attr_name, operation = operation, threshold = str(threshold),
      address = address, msg = urllib.quote(msg))
  return api.xml_value(xml, "triggerId")

def remove_alert(alert_id):
  xml = api.request("removeTrigger", triggerId = str(alert_id))
  return api.xml_value(xml, "retCode")

def alert_info(alert_id):
  xml = api.request("getTrigger", triggerId = alert_id)
  return {
    "device_id": api.xml_value(xml, "devId"),
    "action": api.xml_value(xml, "action"),
    "attr_name": api.xml_value(xml, "attrName"),
    "operation": api.xml_value(xml, "operation"),
    "threshold": float(api.xml_value(xml, "threshold")),
    "address": api.xml_value(xml, "address"),
    "msg": api.xml_value(xml, "msgText"),
    "auto_disarm": api.xml_value(xml, "autoDisarm") == "true",
    "disarmed": api.xml_value(xml, "disarmed") == "true",
  }
