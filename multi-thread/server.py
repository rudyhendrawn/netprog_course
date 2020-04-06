#Simple Echo server using thread to handle multiple connections at a time.
import threading, socket, sys


#The function handlechild handles each client.
def handlechild(clientsock):
	print('New child {}'.format(threading.currentThread().getName()))
	print('Got the connection from {}'.format(clientsock.getpeername()))
	while 1:
		# clientsock, address = socket.accept()
		data = clientsock.recv(2096)		
		if data:
			clientsock.send(data)
			print('{} send: {}'.format(clientsock.getpeername(), data))
		elif data == 'q' or data == 'Q':
			print('Client {} was quit'.format(clientsock.getpeername()))
			clientsock.close()
			break
			
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('localhost', 5300))
	s.listen(5)
	print('Waiting for connection on port 5200')

except socket.error as message:
	if s:
		s.close()
	print ('Couldn\'t open the socket {}'.format(message))
	sys.exit(1)

while 1:
	clientsocket, clientaddress = s.accept()
	t = threading.Thread(target=handlechild, args=[clientsocket])
	daemon = True
	t.start()
