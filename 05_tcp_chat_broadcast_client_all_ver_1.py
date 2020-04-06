import sys, socket, errno
from threading import *

def send_msg(s):
	while True:
		try:
			msg = sys.stdin.readline()
			s.send(msg)
			sys.stdout.write('[Me] ')
			sys.stdout.flush()
		except socket.error as err:
			if err.errno == errno.ECONNRESET:
				sys.stdout.write('Connection to server is disconnected!')
			elif err.errno == errno.ECONNABORTED:
				sys.stdout.write('Connection to server is aborted!')
			break

def recv_msg(sock):
	while True:
		try:
			data = sock.recv(4096)
			if not data :
				print('\nDisconnected from chat server')
				sys.exit()
			else:
				#print data
				sys.stdout.write(data)
				sys.stdout.write('[Me] ')
				sys.stdout.flush()
		except socket.error as err:
			if err.errno == errno.ECONNRESET:
				sys.stdout.write('Connection to server is disconnected!')
			elif err.errno == errno.ECONNABORTED:
				sys.stdout.write('Connection to server is aborted!')
			break

def chat_client():
	if len(sys.argv) < 3:
		print('Usage: python chat_client.py hostname port')
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect to remote host
	try:
		s.connect((host, port))
	except:
		print('Unable to connect')
		sys.exit()

	print('Connected to remote host. You can start sending messages')
	sys.stdout.write('[Me] ')
	sys.stdout.flush()

	t_send = Thread(target=send_msg, args=(s,))
	t_recv = Thread(target=recv_msg, args=(s,))

	try:
		t_send.start()
		t_recv.start()
	except Exception:
		t_send._stop()
		t_recv._stop()
		sys.exit()
	except socket.error as err:
		if err.errno == errno.ECONNRESET:
			sys.stdout.write('Connection to server is disconnected!')
		elif err.errno == errno.ECONNABORTED:
			sys.stdout.write('Connection to server is aborted!')
		t_send._stop()
		t_recv._stop()
		sys.exit()

if __name__ == "__main__":
	sys.exit(chat_client())
