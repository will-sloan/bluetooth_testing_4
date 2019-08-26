from bluetooth import *
target_name = "Automatic Lights"
target_address = None
nearby_devices = discover_devices(flush_cache=True, duration=10)

for address in nearby_devices:
	print(address)
	if target_name == lookup_name( address ):
		target_address = address
		break

if target_address is not None:
	print("found target bluetooth device with address ", target_address)
else:
	print("could not find target bluetooth device nearby")

# Pin passkey 839022
