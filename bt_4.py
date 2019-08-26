from bluetooth import * 

def search():
	while True:
		devices = discover_devices(lookup_names=True)
		yield devices

for a in search():
	print(a)
