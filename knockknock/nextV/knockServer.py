# knockknock.py
from socket import *
import random
import os
import threading


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
        if msg.strip() != "":
            print(msg)
    return msg


def hasPuncuation(string):
    if string.find(".") != -1:
        return 1
    elif string.find(",") != -1:
        return 1
    elif string.find("?") != -1:
        return 1
    elif string.find("!") != -1:
        return 1
    else:
        return 0


def hearJokeFrom(clientsocket, lines, lock):

    while True:
        # recieve message from client
        msg = recieve(clientsocket)
        if "Knock-Knock" in msg:
            # respond "Who's there?" to client
            respond("\tWho's there?", clientsocket)
        else:
            firstPart = msg.strip()
            if hasPuncuation(firstPart) == 1:
                clientsocket.close()
                return 0
            # respond to server
            respond("\t" + str(msg.strip()) + " who?", clientsocket)
            # recieve message from client
            msg = recieve(clientsocket)
            secondPart = msg.strip()
            # respond("haha!", clientsocket)

            alreadyHaveJoke = False
            # print("got here 1")
            for line in lines:
                # print(line[0].strip())
                # print(line[1].strip())
                # print("Hello", firstPart, secondPart)
                if firstPart.lower() == line[0].lower():
                    alreadyHaveJoke = True
                    respond("\tI've heard that one before", clientsocket)
            if not alreadyHaveJoke:
                respond("\tHa Ha!", clientsocket)
                lines.append((firstPart.strip(), msg.strip()))
                newJoke = firstPart, msg
                lock.acquire()
                jokes = open("jokes.txt", "a")
                print("\n" + newJoke[0] + ", " + newJoke[1].strip(), end="", file=jokes)
                jokes.close()
                lock.release()
                clientsocket.close()
            print("Waiting...")
            break


def tellJokeTo(clientsocket, lines):

    # responds to client
    respond("Knock-Knock", clientsocket)
    while True:
        # receives responce from client
        msg = recieve(clientsocket)
        # responds to client with a joke from the file
        if "ho's there" in msg:
            rand = random.randint(0, len(lines)-1)
            respond(lines[rand][0], clientsocket)
        elif " who?" in msg:
            # responds to client with second half of joke
            respond(lines[rand][1].strip(), clientsocket)
            break


def KnockKnock():


    # open socket
    os.system("clear")
    print("...Starting Server...")
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.bind((getMyIp(), 2000))
    serversocket.listen(5)
    print("...Listening...")

    jokes = open("jokes.txt", "r")
    lines = []
    for row in jokes:
        items = row.strip().split(",")
        for thing in items:
            thing = thing.strip()
        lines.append(tuple((items[0].strip(" "), items[1].strip(" "))))
    jokes.close()

    dont_stop = True
    while dont_stop:
        print("Waiting...")
        # receives connection
        clientsocket, addr = serversocket.accept()
        print("connection from : ", addr[0])
        msg = recieve(clientsocket, False)
        if msg == "Tell":
            lock = threading.Lock()
            thread = threading.Thread(target=hearJokeFrom, args=(clientsocket, lines, lock))
            thread.start()
            # print("got here")
        elif msg == "Hear":
            threading.Thread(target=tellJokeTo, args=(clientsocket, lines)).start()

    clientsocket.close()

KnockKnock()
