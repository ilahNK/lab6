#CLIENTcode2

import socket

cSocket = socket.socket()
host = '192.168.1.6'
port = 8881

print('Waiting for connection.')
try: 
	cSocket.connect((host,port))
except socket.error as e:
	print(str(e))

Response = cSocket.recv(1024)
print(Respone)

print("Select operation.")
print("1.log")
print("2.Square root")
print("3.exp")

while True:
	choice = input("Enter choice(1/2/3): ")
	cSocket.send(str.encode(choice))
	if choice in ('1', '2', '3'):
		num1 = input("Enter number:")
		cSocket.send(str.encode(num1))
	else:
		print("Invalid Input")
	
	cSocket.send(str.encode(num1))
	Respone = cSocket.recv(1024)
	print(Respone.decode('utf-8'))
	print(type(Respone))

cSocket.close()

