from bluetooth import *
from temp_sensor import temp
from light_sensor import light
from time import sleep
import traceback

#def return_message(message):
#	sock = BluetoothSocket(RFCOMM)
#	try:
#		sock.connect(client_info)
#		if message == 'temp':
#			sock.send(temp())
#		elif message == 'light':
#			sock.send(temp())
#		else:
#			pass
#		sock.close()
#	except Exception as err:
#		print(f"Connection error {err}")

port = 1






d = {
"temp" : temp,
"light": light
}

def wait_and_listen():
	server_sock = BluetoothSocket(RFCOMM)
	server_sock.bind(("", port))
	server_sock.listen(1)
	client_sock, client_info = server_sock.accept()
	print(f"Accepted Connection from {client_info}")
	return client_sock.recv(1024), client_sock, client_info, server_sock

while True:
	data = None
	data, client_sock, client_info, server_sock = wait_and_listen()
	print("Data is ", data)
	if not data:
		continue
	#if type(data) == bytes:
	data = bytes.decode(data)
	
	print("Received data")
	if data == "temp" or data == "light":
		client_sock.send(d[data]())
	elif data == 'quit':
		client_sock.close()
		server_sock.close()
		break
	elif data:
		client_sock.send(data[::-1])
	else:
		continue
		
	#except Exception as err:
		#print(f"Message error {err}")
	server_sock.close()
	




