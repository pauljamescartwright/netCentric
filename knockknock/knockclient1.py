# knockknockclient.py
import os

from socket import *


def getServerIp():
    responce = input("Enter the servers IP:")
    if responce.strip() == "":
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        SimpleClient(s.getsockname()[0])
    else:
        SimpleClient(responce.strip())


def respond(responce, clientsocket):
    print(responce)
    clientsocket.send(responce.encode("ascii"))


def recieve(clientsocket):
    data = clientsocket.recv(1024)
    msg = data.decode("ascii")
    print(msg)
    return msg


def SimpleClient(IP):

    # connect to server
    os.system("clear")
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((IP, 2000))

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

getServerIp()
