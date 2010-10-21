import geotiq

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
  print "set led1:", geotiq.device_attribute(device, "led1", "0")



# email trigger alert (add remove update)
# twitter trigger alert (add remove update)
# alert list
# error codes