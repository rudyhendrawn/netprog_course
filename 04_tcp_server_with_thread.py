#!/usr/bin/env python

import socket,errno,sys
from _thread import *

HOST = ''
PORT = 1332

def clientTread(conn, addr):
    conn.send('Selamat datang di server Echo. Ketik sesuatu diakhiri dengan tombol ENTER\n')
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            print('Pesan dari {}: {}'.format(addr, data))
            conn.sendall(data)
    
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Socket created')

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        if msg.errno == errno.EADDRINUSE:
            print('Bind gagal.Cek IP dan Port')
            sys.exit()

    print('Socket bind ke port %d' % (PORT))

    s.listen(5)

    print('Socket sedang listening')

    while 1:
        try:
            conn, addr = s.accept()
            print('Terhubung dengan %s dari port %d' % (addr[0], addr[1]))
            start_new_thread(clientTread, (conn, addr[0], ))
        except socket.error as e: 
            if e.errno == errno.ECONNREFUSED: 
                print('gagal melakukan koneksi balik')
            elif e.errno ==  errno.ECONNRESET: 
                print('koneksi ke client terputus')
            elif e.errno == errno.ETIMEDOUT: 
                print('koneksi timeout!')
            else: print(e)    
        except KeyboardInterrupt:
            print('Server dimatikan')
            sys.exit()
        
    s.close()

if __name__ == '__main__':
    main()
