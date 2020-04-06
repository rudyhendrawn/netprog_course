#Simple Echo server using thread to handle multiple connections at a time.
import threading, socket, sys


#The function handlechild handles each client.
def handlechild(clientsock):
	print('New child {}'.format(threading.currentThread().getName()))
	print('Got the connection from {}'.format(clientsock.getpeername()))
	while 1:
		data=clientsock.recv(2096)
		if data == 'q' or data == 'Q':
			print('Client {} was quit'.format(clientsock.getpeername()))
			clientsock.close()
			break
		print('{} send: {}'.format(clientsock.getpeername(), data))
		clientsock.send(data)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost',5300))
	s.listen(5)
	print('Waiting for connection on port 5200')

except socket.error, (value, message):
	if s:
		s.close()
	print ('Couldn\'t open the socket {}',message)
	sys.exit(1)

while 1:
	clientsocket, clientaddress = s.accept()
	t = threading.Thread(target=handlechild, args=[clientsocket])
	daemon = True
	t.start()
