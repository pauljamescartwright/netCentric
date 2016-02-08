# knockknock.py
from socket import *
import random
import os


def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])


def respond(responce, clientsocket):
    print(responce)
    clientsocket.send(responce.encode("ascii"))


def recieve(clientsocket):
    data = clientsocket.recv(1024)
    msg = data.decode("ascii")
    print(msg)
    return msg


def hearJoke(clientsocket):
    # recieve data from server
    msg = recieve(clientsocket)

    # respond to server
    respond("\tWho's there?", clientsocket)

    # recieve data from server
    msg = recieve(clientsocket)

    # respond to server
    respond(str("\t" + str(msg) + " who?"), clientsocket)

    # recieve data from server
    msg = recieve(clientsocket)

def tellJoke(clientsocket):

    # responds to client
    respond("Knock-Knock", clientsocket)

    # receives responce from client
    msg = recieve(clientsocket)

    # responds to client with a joke from the file
    if msg == "\tWho's there?":
        jokes = open("jokes.txt")
        lines = []
        for row in jokes:
            items = row.strip().split(",")
            lines.append(tuple(items))
        rand = random.randint(0, len(lines)-1)
        respond(lines[rand][0], clientsocket)

    # receives responce from client
    msg = recieve(clientsocket)

    # responds to client with second half of joke
    respond(lines[rand][1].strip(), clientsocket)


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
        msg = recieve(clientsocket)
        if msg == "tell":
            tellJoke(clientsocket)
        else: 
            hearJoke(clientsocket)

    clientsocket.close()

KnockKnock()
