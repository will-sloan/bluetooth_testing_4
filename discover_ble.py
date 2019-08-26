from bluetooth import *

service = DiscoveryService()

devices = service.discover(2)

print(devices)
