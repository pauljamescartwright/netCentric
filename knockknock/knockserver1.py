# knockknock.py
from socket import *
import random
import os


def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])


def KnockKnock():
    # open socket
    os.system("clear")
    print("...Starting Server...")
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.bind((getMyIp(), 2000))
    serversocket.listen(1)
    print("...Listening...")

    # starting loop
    dont_stop = True
    while dont_stop:
        print("Waiting...")

        # receives connection
        clientsocket, addr = serversocket.accept()
        print("connection from : ", addr[0])

        # responds to client
        responce = "Knock-Knock"
        print(responce)
        clientsocket.send(responce.encode("ascii"))

        # receives responce from client
        data = clientsocket.recv(1024)
        msg = data.decode("ascii")
        print(msg)

        # responds to client with a joke from the file
        if msg == "\tWho's there?":
            jokes = open("jokes.txt")
            lines = []
            for row in jokes:
                items = row.strip().split(",")
                lines.append(tuple(items))
            rand = random.randint(0, len(lines)-1)
            responce = lines[rand][0]
            print(responce)
            clientsocket.send(responce.encode("ascii"))

        # receives responce from client
        data = clientsocket.recv(1024)
        msg = data.decode("ascii")
        print(msg)

        # responds to client with second half of joke
        responce = lines[rand][1]
        responce = responce.strip()
        print(responce)
        clientsocket.send(responce.encode("ascii"))

    clientsocket.close()

KnockKnock()
