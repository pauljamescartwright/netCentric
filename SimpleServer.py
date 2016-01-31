 #SimpleServer.py
import time;
from socket import *
import random
import os

def getMyIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return (s.getsockname()[0])

def SimpleServer():
    os.system("clear")
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.bind((getMyIp(),2000))
    serversocket.listen(1)
    print("...Starting Server...")
    dont_stop = True
    while dont_stop == True:
        clientsocket,addr = serversocket.accept()
        print("connection from : ", addr[0])
        data = clientsocket.recv(1024)
        msg = data.decode("ascii")
        if msg == "whoareyou?":
            clientsocket.send(gethostname().encode("ascii"))
        elif msg == "whenisit?":
            clientsocket.send(str(time.asctime( time.localtime(time.time()) )).encode("ascii"))
        elif msg == "whatdidyousay?":
            words = open("words")
            list = []
            for line in words:
                list.append(line.strip())
            num = random.randint(0, len(list))
            word = list[num]
            clientsocket.send(str(word).encode("ascii"))
        elif msg[:4] == "add,":
            msg_list = msg.split(",")
            sum = int(msg_list[1]) + int(msg_list[2])
            clientsocket.send(str(sum).encode("ascii"))
        elif msg == "bye!":
            dont_stop = False
            clientsocket.send("See you later!".encode("ascii"))
        elif msg == "help":
            clientsocket.send("Who I am: \"whoareyou?\"\nWhen it is: \"whenisit?\"\nWhat I said: \"whatdidyousay?\"\nAdding numbers x and y: \"add,x,y\"\nWhen you want to hangup: \"bye!\"".encode("ascii"))
        else:
            clientsocket.send(str("Huh? : " + msg + "\nWho I am: \"whoareyou?\"\nWhen it is: \"whenisit?\"\nWhat I said: \"whatdidyousay?\"\nAdding numbers x and y: \"add,x,y\"\nWhen you want to hangup: \"bye!\"").encode("ascii"))
        clientsocket.close()
    #serversocket.close()

SimpleServer()
