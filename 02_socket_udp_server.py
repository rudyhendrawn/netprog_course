import socket

IP='127.0.0.1'
PORT=666

sck = socket.socket(socket.AF_INET, # Address Family INterNET
                    socket.SOCK_DGRAM) # UDP

try:
    sck.bind((IP, PORT))
    print ("Bind ke IP %s dengan port %s" % (IP, PORT))
    while 1:
        conn, addr = sck.recvfrom(1024)
        print ("Ada pesan dari IP %s" % (addr[0]))
        print ("Isi pesan: %s" % (conn))
        print ("-----------------------------")
        if not conn: 
            break
    conn.close()
except socket.error as msg:
    print ("Error! %s" % (msg))

except Exception as e :
    print ("Ops, coding salah! %s" % (e))
