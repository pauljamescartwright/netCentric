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


def respond(responce, clientsocket, printresponce=True):
    if printresponce:
        print(responce)
    clientsocket.send(responce.encode("ascii"))


def recieve(clientsocket, printresponce=True):
    data = clientsocket.recv(1024)
    msg = data.decode("ascii")
    if printresponce:
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
    print("joke to server")
    # receives responce from client
    respond("\tKnock-Knock", clientsocket)
    while(True):
        msg = recieve(clientsocket)
        if msg == "haha!":
            break
        else:
            usrInput = input("\t")
            respond("\t" + usrInput, clientsocket, False)



def SimpleClient(IP):
    # connect to server
    os.system("clear")
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((IP, 2000))

    # ask for input
    done = False
    while not done:
        usrInput = int(input("Do you want to tell a joke(0) or hear a joke(1)"))
        if usrInput == 1:
            respond("hear", clientsocket, False)
            hearJoke(clientsocket)
            done = True
        elif usrInput == 0:
            respond("tell", clientsocket, False)
            tellJoke(clientsocket)
            done = True


getServerIp()
