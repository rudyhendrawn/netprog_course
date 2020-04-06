import socket 
import sys 
host = 'localhost' 
port = 50000 
size = 1024 
s = None 
try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((host,port)) 
except socket.error, (value, message): 
	if s: 
		s.close() 
	print('Could not open socket: {}'.format(message))
	sys.exit(1) 

while True:
	data = raw_input('Type Something(q or Q to exit:)')
	s.send(data)
	if data == 'q' or data == 'Q':
		s.close()
		break
	else:
		newdata = s.recv(size)
		print newdata

               
