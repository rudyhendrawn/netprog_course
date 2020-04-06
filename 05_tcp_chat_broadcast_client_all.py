#!/usr/bin/env python2
# chat_client.py

import sys, socket, select
from threading import *

def send_msg(s):
    while True:
        msg = sys.stdin.readline()
        s.send(msg)
        sys.stdout.write('[Me] '); sys.stdout.flush()

def recv_msg(sock):
    while True:
        data = sock.recv(4096)
        if not data :
            print('\nDisconnected from chat server')
            sys.exit()
        else :
            #print data
            sys.stdout.write(data)
            sys.stdout.write('[Me] '); sys.stdout.flush()

def chat_client():
    if(len(sys.argv) < 3) :
        print('Usage : python chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. You can start sending messages')
    sys.stdout.write('[Me] '); sys.stdout.flush()

    Thread(target=send_msg, args=(s,)).start()
    Thread(target=recv_msg, args=(s,)).start()

if __name__ == "__main__":
    sys.exit(chat_client())