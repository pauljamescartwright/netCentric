#SimpleClient.py
import os

from socket import *

def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])

def SimpleClient():
    os.system("clear")
    keepgoing = True
    while keepgoing == True:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((getMyIp(),2000))
        print("\n*1...Enter Command.\n*2...Help?\n*0...Quit!")
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
SimpleClient()