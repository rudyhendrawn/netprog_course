import socket, sys
host = '' 
port = 50000 
backlog = 5 
size = 1024 
s = None 
try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host,port)) 
	s.listen(backlog) 
	print('The server is listening on port: 50000')
except socket.error, (value,message): 
	if s: 
		s.close() 
	print('Could not open socket: {}'.format(message))
	sys.exit(1) 
while True: 
	client, address = s.accept() 
	print('Received the connection from: {}'.format(address))
	while True:
		data=client.recv(size)
		if data=='q' or data=='Q':
			client.close()
			print('Client quits:')
			break
		else:
			print('Data received: {}'.format(data))
			newdata = 'You Send:' + data
			client.send(newdata)

			
		

	

