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


def respond(responce, client):
    print(responce)
    client.send(responce.encode("ascii"))


def recieve(client):
    data = client.recv(1024)
    msg = data.decode("ascii")
    print(msg)
    return msg


def SimpleClient(IP):
    # connect to server
    os.system("clear")
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP, 2000))
    print("...Conected...")

    # recieve data from server
    msg = recieve(client)

    # respond to server
    respond("\tWho's there?", client)

    # recieve data from server
    msg = recieve(client)

    # respond to servers
    if msg == "Banana":
        respond(str("\t" + str(msg) + " who?"), client)
        msg = recieve(client)
        respond(str("\t" + "BANANA" + " who!?"), client)
        msg = recieve(client)
        respond(str("\t" + str(msg) + " who?"), client)
    else:
        respond(str("\t" + str(msg) + " who?"), client)

    # recieve data from server
    msg = recieve(client)

getServerIp()
