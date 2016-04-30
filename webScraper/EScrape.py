
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random




def readTable(url):
    html= urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    element = bs.findAll("table", {"class":"elections_states"})
    
    
    try:
        nameTable = element[1] 
    except IndexError:
        nameTable = element
        
        #print (element)
    

    bsData = nameTable.findAll('tr')
    canidateNames = []
    canidateParties = []

    for i in range(len(bsData)-2):
        canid = list(bsData[i+2].children)
        canidateNames.append(canid[7].getText().strip())
        canidateParties.append(canid[3].getText().strip())

    for i in range(len(canidateNames)):
        print(canidateNames[i], canidateParties[i])

    #print(50*"#")






def getPage():    #!!!!!this is the function that will start and end the program!!!!!
    date = 1940
    while (date <= 2012):
        print(date)
        if (date != 1976):
            url = "http://www.presidency.ucsb.edu/showelection.php?year=" + str(date)
            readTable(url)
        date = date + 4
    
getPage()
    
#readTable("http://www.presidency.ucsb.edu/showelection.php?year=1940") #1976

