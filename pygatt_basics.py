import pygatt
import time
adapter = pygatt.GATTToolBackend()

def handle_data(handle, value):
	print(f"Received data {bytes.decode(value)}")

try:
	adapter.start()
	device = adapter.connect('CA:34:A7:E4:DF:50')
	
	print("Connected")
finally:
	adapter.stop()
