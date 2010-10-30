import geotiq
import time

geotiq.login("dan", "thebeast")

# device list
devices = geotiq.devices()

for device in devices:
  print "device_id", device

  # device status
  print "connected:", geotiq.device_status(device)

  # device attributes
  for name, value in geotiq.device_attributes(device).iteritems():
    print "%s: %s" % (name, value)

  # set device attribute
  print "set led1 to 0:", geotiq.device_attribute(device, "led1", 0)

  # add alert to device
  print "added alert:", \
        geotiq.add_alert(device, "email", "temp", ">=", "70", "dmacdougall@gmail.com", "it is hot!")

  # remove all alerts from device
  for alert in geotiq.alerts(device):
    return_code = geotiq.remove_alert(alert)
    print "removed alert %s with status %s" % (alert, return_code)

# error codes