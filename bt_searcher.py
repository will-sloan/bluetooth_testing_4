
from bluetooth import *

nearby_devices = discover_devices(lookup_names=True, duration=10)
print(nearby_devices)
'''	
for service in services:
	print(service)
for address in nearby_devices:
	print(address)

if nearby_devices:
	print("found target bluetooth device with address ", nearby_devices)
	print("found services of ", service)
else:
	print("could not find target bluetooth device nearby")

'''
