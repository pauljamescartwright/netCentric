# mockDNS.py

from socket import *
from time import *
from threading import *
import random


def getIPAddress():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def getMessage(client):

    data = client.recv(1024)
    # print(data)
    return data.decode('ascii')


def getHosts():
    hostFile = open("hosts.txt", "r")
    hostDict = {}

    for line in hostFile:
        line = line.strip()
        (key, value) = line.split(",")
        hostDict[key] = value

    hostFile.close()
    return hostDict


def updateHosts(hosts):
    hostFile = open("hosts.txt", "w")

    print("Updating")

    for entry in hosts:
        print(entry, ",", hosts[entry], file=hostFile, sep="")
    hostFile.close()


def processRequest(cs, addr, hosts, lock):

    print ("Connnection from " + str(addr))
    try:
        (rID, ip) = getMessage(cs).split(",")

        print("id: " + rID + "\nip: " + ip)

        if (rID == "all"):
            cs.send("Naughty Naughty".encode('ascii'))
            cs.close()

        else:
            if (ip == addr[0]):
                if rID not in hosts:
                    print("Not Found")
                    lock.acquire()
                    hosts[rID] = ip
                    updateHosts(hosts)
                    lock.release()

                if str(hosts[rID]) == ip:
                    cs.send("OK".encode('ascii'))

                who = getMessage(cs)
                print(who)

                if who[:4] == "who ":
                    who = who[4:]
                    msg = ""

                    if who == "all":
                        for ID in hosts:
                            msg += ID + ","+hosts[ID]+"\n"
                    elif who in hosts:
                        msg = str(hosts[who])
                    else:
                        msg = "Not Found"

                    cs.send(msg.encode('ascii'))
                    print("Returned: " + msg)

            else:
                cs.close()

    except ConnectionResetError:
        print("Connection from ", addr, "reset")


def mockDNSServer():

    lock = Lock()
    hosts = getHosts()
    port = 2053

    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    host = getIPAddress()
    print("Listening on ", host)

    serversocket.bind((host, port))
    serversocket.listen(5)

    while True:
        print("Waiting")
        cs, addr = serversocket.accept()
        Thread(target=processRequest, args=(cs, addr, hosts, lock)).start()

mockDNSServer()
