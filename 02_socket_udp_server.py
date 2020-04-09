import socket

IP = '127.0.0.1'
PORT = 666

sck = socket.socket(socket.AF_INET, # Address Family INterNET
                    socket.SOCK_DGRAM) # UDPs

try:
    sck.bind((IP, PORT))
    print ('Bind ke IP {} dengan port {}'.format(IP, PORT))
    while 1:
        conn, addr = sck.recvfrom(1024)
        print ('Ada pesan dari IP {}'.format(addr[0]))
        print ('Isi pesan: {}'.format(conn))
        print ('-----------------------------')
        if not conn: 
            break
    conn.close()
except socket.error as msg:
    print ('Error! {}'.format(msg))

except Exception as e :
    print ('Ops, coding salah! {}'.format(e))
