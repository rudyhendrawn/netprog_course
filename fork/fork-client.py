import socket


clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost', 50007))
print('Enter q or Q to quits:')

while 1:
  data = input('>')
  data = bytes(data, 'utf-8')
  clientsocket.send(data)
  if data == 'q' or data == 'Q':
    break
  newdata = clientsocket.recv(1024)
  print(newdata)

clientsocket.close()