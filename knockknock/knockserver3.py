# knockknock.py
from socket import *
import random
import os


def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])


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


def hearJoke(clientsocket, lines):
    # recieve data from server
    msg = recieve(clientsocket)

    # respond to server
    respond("Who's there?", clientsocket)

    # recieve data from server
    msg = recieve(clientsocket)
    firstPart = msg

    # respond to server
    respond(str(msg.strip()) + " who?", clientsocket)

    # recieve data from server
    msg = recieve(clientsocket)

    alreadyHaveJoke = False
    for line in lines:

        if firstPart == line[0] and msg == line[1]:
            alreadyHaveJoke = True
    if not alreadyHaveJoke:
        lines.append((firstPart.strip(), msg.strip()))
        newJoke = firstPart + ", " + msg
    respond("haha!", clientsocket)
    return newJoke


def tellJoke(clientsocket, lines):

    # responds to client
    respond("Knock-Knock", clientsocket)

    # receives responce from client
    msg = recieve(clientsocket)

    # responds to client with a joke from the file
    if msg == "\tWho's there?":
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

    jokes = open("jokes.txt", "r+")
    lines = []
    for row in jokes:
        items = row.strip().split(",")
        lines.append(tuple(items))

    dont_stop = True
    while dont_stop:
        print("Waiting...")
        # receives connection
        clientsocket, addr = serversocket.accept()
        print("connection from : ", addr[0])
        msg = recieve(clientsocket, False)
        if msg == "tell":
            newJoke = hearJoke(clientsocket, lines)
            # jokes.write("\n" + newJoke.strip())
            # jokes.close()
        else:
            tellJoke(clientsocket, lines)

    clientsocket.close()

KnockKnock()
