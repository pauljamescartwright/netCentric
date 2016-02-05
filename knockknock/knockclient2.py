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

    ### connect to server
    os.system("clear")
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP,2000))

    ### recieve data from server
    msg = client.recv(1024)
    print(msg.decode("ascii"))

    ### respond to server
    responce = "\tWho's there?"
    print(responce)
    client.send(responce.encode("ascii"))

    ### recieve data from server
    data = client.recv(1024)
    msg = data.decode("ascii")
    print(msg)

    ### respond to server
    responce = str("\t" + str(msg) + " who?")
    print(responce)
    client.send(responce.encode("ascii"))

    ### recieve data from server
    data = client.recv(1024)
    msg = data.decode("ascii")
    print(msg)

getServerIp()