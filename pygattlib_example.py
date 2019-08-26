from gattlib import DiscoveryService

service = DiscoveryService("hci0")
devices = service.discover(4)

for address, name in list(devices.items()):
    print("name: {}, address: {}".format(name, address))

print("Done.")
