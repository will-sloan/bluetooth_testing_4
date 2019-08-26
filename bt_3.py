from bluetooth import *
port = 1

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", port))
server_sock.listen(1)
client_sock, client_info = server_sock.accept()
print(f"Accepted Connection from {client_info}")

while True: 
	data = client_sock.recv(1024)
	if not data:
		break
	data = bytes.decode(data)
	print("Received ", data)
	client_sock.send(data[::-1])

server_sock.close()
client_sock.close()
