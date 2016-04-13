
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def presidents():

    html= urlopen("https://en.wikipedia.org/wiki/United_States_presidential_election,_1824")
    bsObj = BeautifulSoup(html, "html.parser")

    print(bsObj.findAll("table", {"class": re.compile("sortable")}))
    print("hello")

presidents()

