import threading, socket, sys

try: 
  c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  c.connect(('localhost', 5300))
  
except socket.error as message:
    if c:
      c.close()
    print('Couldn\'t open the socket {}'.format(message))
    sys.exit(1)


while True:
  data = input('Enter data to send: ')   
  if data == 'q' or data == 'Q':
     c.send(data.encode('utf-8'))
     break
  c.send(data.encode('utf-8'))
  print('Received data: {}'.format(c.recv(1024)))



  
