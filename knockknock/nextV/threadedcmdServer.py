
#SimpleServer.py
#Study http://docs.python.org/3/library/socket.html  for more info on sockets

from socket import *
from time import *
import threading


def processRequest(clientsocket):

    done = False
    while not done:
        data = clientsocket.recv(1024)
        if data:
            cmd = data.decode('ascii')
            if cmd == "Hello":
                clientsocket.send("Hi".encode('ascii'))
            elif cmd == "Who":
                clientsocket.send(gethostname().encode('ascii'))
            elif cmd == "When":    
                currentTime = ctime(time())
                clientsocket.send(currentTime.encode('ascii')) 
            elif cmd =="Bye":
                clientsocket.close()
                done = True
            else:
                clientsocket.send("huh".encode('ascii'))
        


def cmdServer():
    #create a socket object
    #   socket is a function that returns a variable of type socket (a constructor)
    #   AF_INET is the Address Format:Internet -- you are going to connect with an IP Address
    #   SOCK_STREAM it the type of socket --- how to package the data.
    serversocket = socket(AF_INET, SOCK_STREAM)

    #allow your server to reuse the address instead of waiting for a timeout
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    #Be sure that your socket communicates on it's IP address, on a specific port
    #   The port is 2000 -- this was chosen somewhat randomly
    #   NOTE: bind takes a tuple, not two parameters.
    
    serversocket.bind(("192.168.1.37", 2000))

    #Start listening for requests.
    #   Argument is the size of the request buffer
    serversocket.listen(5)

    #Block here until there is a request
    #   when you accept, you should know 2 values
    #   clientsocket and addr (who connected to you)

    while True:
        print("Waiting")
        clientsocket,addr = serversocket.accept()
        print ("Connnection from", addr)
        threading.Thread(target=processRequest, args=(clientsocket,)).start()

        
        



