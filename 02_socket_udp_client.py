import socket

IP = '127.0.0.1'
PORT = 666
PESAN = 'hi, apa kabar?'

sck = socket.socket(socket.AF_INET, # Address Family INterNET
                    socket.SOCK_DGRAM) # UDP

try:
    # cara 1
    sck.sendto(PESAN, (IP, PORT))
    # cara 2
    #sck.connect((IP,PORT))
    #sck.send(PESAN) 
except socket.error as msg:
    print('Error! {}'.format(msg))

except Exception as err:
    print('Ops, coding salah! {}'.format(err))

finally:
    sck.close()