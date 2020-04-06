import os, time, sys
from socket import *     


myHost = ''                               
myPort = 50007                            
sockobj = socket(AF_INET, SOCK_STREAM) # create a TCP socket object
sockobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockobj.bind((myHost, myPort)) # bind it to server port number
print('The server is listening on port 50007')
sockobj.listen(5) # allow 5 pending connects

activeChildren = []

def reapChildren(): # reap any dead child processes
    while activeChildren: # else may fill up system table
        pid, stat = os.waitpid(0, os.WNOHANG) # don't hang if no child exited
        if not pid:
            break
        else:
            activeChildren.remove(pid)
            print('Reaped Child Process: {}'.format(pid))

def handleClient(connection): # child process: reply, exit
    while True:  # read, write a client socket
        data = connection.recv(1024) # till eof when socket closed
        if data == 'q' or data == 'Q':
	        connection.close()
	        break
        else:
            newdata = 'You send:' + data
            connection.send(newdata)
    os._exit(0)


def dispatcher():# listen until process killed
    while True: # wait for next connection,
        connection, address = sockobj.accept() # pass to process for service
        reapChildren() # clean up exited children now
        childPid = os.fork()  # copy this process
        if childPid == 0: # if in child process: handle
            handleClient(connection)
        else: # else: go accept next connect
            activeChildren.append(childPid) # add to active child pid list


dispatcher() # call the function dispatcher.

