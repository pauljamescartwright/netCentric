# knockknockclient.py
import os
import mockDNSClient
from socket import *
import time
import random

def getServerIp():
    print(mockDNSClient.mockDNSClient("192.168.1.235", "all"))
    found = False
    while not found:
        usrInput = input("Who do you want ask/tell a joke to? : ")
        #if usrInput == "all":
        #    

        hostIP = mockDNSClient.mockDNSClient("192.168.1.235", usrInput)
        if hostIP != "Not Found":
            found = True
    SimpleClient(hostIP)


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


def hearJoke(clientsocket, listOf, lines):
    # while True:
    msg = recieve(clientsocket)
    # if "Knock-Knock" in msg:
    # respond to server
    respond("\tWho's there?", clientsocket)
    msg = recieve(clientsocket)
    firstPart = msg
    found = False
    for item in listOf:
        if item[0] == firstPart:
            found = True
            item[1] += 1
    if found == False:
        listOf.append([firstPart, 1])
    respond(str("\t" + str(msg) + " who?"), clientsocket)
    msg = recieve(clientsocket)
    secondPart = msg
    # for item in lines:
        # if firstPart.lower() in item[0].lower():
            # lines.append((firstPart, secondPart))
            # jokes = open("Clientjokes.txt", "a")
            # print(firstPart + ", " + secondPart, file=jokes)
            # jokes.close()


def tellJoke(clientsocket, lines, askUsr=False):
    if askUsr:
        name = input("Please Enter the Name: ")
        punchline = input("Punchline Please:      ")
        lines.append((name, punchline))
        jokes = open("Clientjokes.txt", "a")
        print(name + ", " + punchline, file=jokes)
        jokes.close()
    rand = random.randint(0, len(lines)-1)
    respond("Knock-Knock", clientsocket)
    msg = recieve(clientsocket)
    if askUsr:
        respond(name, clientsocket)
    else:
        respond(lines[rand][0], clientsocket)
    msg = recieve(clientsocket)
    if askUsr:
        respond(punchline, clientsocket)
    else:
        respond(lines[rand][1], clientsocket)
    msg = recieve(clientsocket)
    if "Ha Ha!" in msg:
        return True
    elif "head that before" in msg:
        return False


def SimpleClient(IP):
    # connect to server
    # os.system("clear")
    jokes = open("Clientjokes.txt")
    lines = []
    for row in jokes:
        items = row.strip().split(",")
        for thing in items:
            thing = thing.strip()
        lines.append(tuple((items[0].strip(" "), items[1].strip(" "))))
    jokes.close()
    listOf = []
    thing = False
    times = 0
    try:
        while not thing:
            time.sleep(.01)
            clientsocket = socket(AF_INET, SOCK_STREAM)
            clientsocket.settimeout(3)
            clientsocket.connect((IP, 2000))
            respond("Hear", clientsocket, False)
            time.sleep(.01)
            hearJoke(clientsocket, listOf, lines)
            time.sleep(.01)
            clientsocket.close()
            for item in listOf:
                if item[1] >= 4:
                    thing = True
        while True:
            time.sleep(.25)
            clientsocket = socket(AF_INET, SOCK_STREAM)
            clientsocket.settimeout(3)
            clientsocket.connect(("127.0.0.1", 2000))
            respond("Tell", clientsocket, False)
            time.sleep(.25)
            if times >= len(lines):
                var = tellJoke(clientsocket, lines, True)
            else:
                var = tellJoke(clientsocket, lines)
            times += 1
            if var:
                break
    except timeout:
        print("timed out")# ask for input

getServerIp()
