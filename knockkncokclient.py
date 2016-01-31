#knockknockclient.py
import os

from socket import *

def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])

def SimpleClient():
    os.system("clear")
    keepgoing = True
    #while keepgoing == True:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((getMyIp(),2000))
    msg = client.recv(1024)
    print(msg.decode("ascii"))
    responce = "\tWho's there?"
    print(responce)
    client.send(responce.encode("ascii"))
    msg = client.recv(1024)
    print(msg.decode("ascii"))
    responce = str("\t" + str(msg) + " who?")
    print(responce)
    client.send(responce.encode("ascii"))

"""
        print("\n*1...dvfdv.\n*2...Help?\n*0...Quit!")
        usr_input = int(input("Option: *"))
        if usr_input == 1:
            print("Enter Command: ")
            da_input = str(input())
            client.send(da_input.encode("ascii"))
        elif usr_input == 2:
            client.send("help".encode("ascii"))
        elif usr_input == 0:
            client.send("bye!".encode("ascii"))
            keepgoing = False
        os.system("clear")
        msg = client.recv(1024)
        print(msg.decode("ascii"))
"""
SimpleClient()