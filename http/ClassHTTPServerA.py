# classHTTPServer.py

from socket import *
from time import *
from threading import *


def getIPAddress():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def getMessage(client):

    data = client.recv(1024)
    return data.decode('ascii')

kum = 0
rut = 0
def processRequest(cs, addr):
    global kum
    global rut
    print(kum, rut)
    print ("Connnection from " + str(addr))

    data = cs.recv(10000)
    data = data.decode('ascii')
    print(data)

    if "POST" in data[:6]:
        end = data.find("HTTP/1.1") - 1
        request = data[5:end]
        if request == "/Greeting.ss235":
            blankline = data.find("\r\n\r\n")
            query = data[blankline+4:]
            firstLast = query.split("&")
            firstStart = firstLast[0].find("=") + 1
            firstLast[0] = firstLast[0][firstStart:]
            firstname = firstLast[0]
            lastStart = firstLast[1].find("=") + 1
            firstLast[1] = firstLast[1][lastStart:]
            lastname = firstLast[1]
            response = "HTTP/1.1 200 OK \n"
            response += "Content-Type: text/html\n"
            response += "\r\n"
            cs.send(response.encode('ascii'))
            f = open("Greeting.ss235", "r")
            fContents = f.read()
            fContents = fContents.replace("{text here}", firstname + " " + lastname)
            cs.send(fContents.encode('ascii'))
            cs.close()
        elif request == "/Vote.ss235":
            blankline = data.find("\r\n\r\n")
            query = data[blankline+4:]
            print(query)
            if "Kumquat" in query:
                kum += 1
                text = "Thank you for voting for Kumquats.<br />"
            elif "Rutabaga" in query:
                rut += 1
                text = "Thank you for voting for Rutabagas.<br />"
            response = "HTTP/1.1 200 OK \n"
            response += "Content-Type: text/html\n"
            response += "\r\n"
            cs.send(response.encode('ascii'))
            f = open("Vote.ss235", "r")
            fContents = f.read()
            text += "The current vote totals are: Kumquats: " + str(kum) + ", Rutabagas: " + str(rut)
            fContents = fContents.replace("{text here}", text)
            cs.send(fContents.encode('ascii'))
            cs.close()
    else:

        end = data.find("HTTP/1.1") - 1
        request = data[4:end]

        if "%20" in request:
            request = request.replace("%20", " ")

        if request == "/":
            request = "/index.html"

        print("*"+request+"*")

        if "?" in request:
            mark = request.find("?")
            query = request[mark:]
            request = request.replace(query, "")
            print("**" + query + "**")

        if request[-5:] == ".html":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: text/html\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: text/html\n"
                response += "\r\n"
                f = open("errors/404.html", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request[-4:] == ".pdf":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: text/pdf\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: text/html\n"
                response += "\r\n"
                f = open("errors/404.html", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request == "/favicon.ico":
            response = "HTTP/1.1 200 OK \n"
            response += "Content-Type: image/x-icon\n"
            response += "\r\n"
            cs.send(response.encode('ascii'))
            f = open("favicon.ico", "rb")
            cs.send(f.read())

        elif request[-4:] == ".jpg":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: image/jpeg\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: image/png\n"
                response += "\r\n"
                f = open("errors/404.png", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request[-4:] == ".png":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: image/png\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: image/png\n"
                response += "\r\n"
                f = open("errors/404.png", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request[-4:] == ".bmp":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: image/jpeg\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: image/bmp\n"
                response += "\r\n"
                f = open("errors/404.png", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request[-4:] == ".gif":
            try:
                response = "HTTP/1.1 200 OK \n"
                response += "Content-Type: image/gif\n"
                response += "\r\n"
                f = open(request[1:], "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())
            except FileNotFoundError:
                response = "HTTP/1.1 404 OK \n"
                response += "Content-Type: image/png\n"
                response += "\r\n"
                f = open("errors/404.png", "rb")
                cs.send(response.encode('ascii'))
                cs.send(f.read())

        elif request == "/Greeting.ss235":
            response = "HTTP/1.1 200 OK \n"
            response += "Content-Type: text/html\n"
            response += "\r\n"
            f = open("Greeting.ss235", "r")
            fContents = f.read()
            firstLast = query.split("&")
            firstStart = firstLast[0].find("=") + 1
            firstLast[0] = firstLast[0][firstStart:]
            firstname = firstLast[0]
            lastStart = firstLast[1].find("=") + 1
            firstLast[1] = firstLast[1][lastStart:]
            lastname = firstLast[1]
            fContents = fContents.replace("{text here}", firstname + " " + lastname)
            cs.send(response.encode('ascii'))
            cs.send(fContents.encode('ascii'))

        elif request == "/Vote.ss235":
            response = "HTTP/1.1 200 OK \n"
            response += "Content-Type: text/html\n"
            response += "\r\n"
            f = open("Vote.ss235", "rb")
            cs.send(response.encode('ascii'))
            cs.send(f.read())

        else:
            response = "HTTP/1.1 501 OK \n"
            response += "Content-Type: text/html\n"
            response += "\r\n"
            f = open("errors/501.html", "rb")
            cs.send(response.encode('ascii'))
            cs.send(f.read())
        cs.close()


def HTTPServer():

    port = 2080

    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    host = "127.0.0.1"  # getIPAddress()
    print("Listening on ", host)

    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        print("Waiting")
        cs, addr = serversocket.accept()
        Thread(target=processRequest, args=(cs, addr)).start()

HTTPServer()
