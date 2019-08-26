from bluetooth import *

target = "CA:34:A7:E4:DF:50"

sock = BluetoothSocket()
for i in range(1,31):
	try:
		sock.connect((target, i))
		sock.send(1)
	except:
		print("Not this one ", i)
print(sock.recv(512))
sock.close()
