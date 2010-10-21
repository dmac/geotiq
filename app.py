import geotiq

geotiq.auth.login("dan", "thebeast")
print geotiq.api.devices()
