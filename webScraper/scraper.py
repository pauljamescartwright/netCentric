from urllib.request import urlopen
from bs4 import BeautifulSoup

def getPage():
    html = urlopen("http://192.168.1.235/gifts.html")
    bsobj = BeautifulSoup(html.read())
    parrot = bsobj.find(text="\nDead Parrot\n").parent.parent
    priceStart = parrot.find("$")
    priceEnd = parrot[priceStart].find("\n")
    price = parrot[priceStart:priceEnd]
    print(parrot, "costs", price)

getPage()