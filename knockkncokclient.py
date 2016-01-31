#knockknockclient.py
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

def SimpleClient(IP):
    os.system("clear")
    keepgoing = True
    #while keepgoing == True:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP,2000))
    msg = client.recv(1024)
    print(msg.decode("ascii"))
    responce = "\tWho's there?"
    print(responce)
    client.send(responce.encode("ascii"))
    data = client.recv(1024)
    msg = data.decode("ascii")
    print(msg)
    responce = str("\t" + str(msg) + " who?")
    print(responce)
    client.send(responce.encode("ascii"))
    data = client.recv(1024)
    msg = data.decode("ascii")
    print(msg)

getServerIp()