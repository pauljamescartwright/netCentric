# mockDNSClient.py

from socket import *

LHost = "cartwright"


def getIPAddress():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0].strip()


def getMessage(sock):
    data = sock.recv(1024)
    return data.decode('ascii')


def lookUpAddr(hostname):
    # first check locally
    try:
        hostFile = open("Hosts.local", "r")

        for line in hostFile:
            line = line.strip()
            (host, addr) = line.split(",")
            if host == hostname:
                hostFile.close()
                return addr
        hostFile.close()

    except FileNotFoundError:
        pass

    return "0"

def mockDNSClient(host, name):

    port = 2053

    hostIP = lookUpAddr(name)

    if hostIP != "0":
        print("Found Local")
        print (hostIP)
    else:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((host, port))
            myIP = getIPAddress()
            
            print("I am ", LHost,myIP)
            s.send((LHost+","+myIP).encode('ascii'))
            auth = getMessage(s)
            print(auth)  #Should be "ok"
            s.send(("who "+name).encode('ascii'))
            hostIP = getMessage(s)
            print(hostIP)
            if hostIP != "Not Found" and name != "all":
                hostFile = open("Hosts.local", "a")
                print(name+","+hostIP, file=hostFile)
                hostFile.close()
        except ConnectionAbortedError:
            print("Connection terminated; protocol violation")

        s.close()
    return hostIP
