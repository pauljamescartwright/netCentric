
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def presidents(year):
    html= urlopen("https://en.wikipedia.org/wiki/United_States_presidential_election,_" + year)
    bsObj = BeautifulSoup(html, "html.parser")

    thing = bsObj.select('table.wikitable.sortable')
    # bsObj.findAll("table", {"class": re.compile("wikitable")}).findAll("table", {"class": re.compile("sortable")})
    f = open("year"+year, "w")
    print(thing[0], file=f)
    f.close()

def years():
    for i in range(0, 10):
        year = i*4+1824
        presidents(str(year))

years()

