
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def presidents(year):
    html = urlopen("http://www.presidency.ucsb.edu/showelection.php?year=" + year)
    bsObj = BeautifulSoup(html, "html.parser")
    #
    bs = BeautifulSoup(html, "html.parser")
    element = bs.findAll("table", {"class":"elections_states"})
    print(element)
    try:
        nameTable = element[1] 
    except IndexError:
        nameTable = element
    bs1 = BeautifulSoup(str(nameTable), "html.parser")
    print(nameTable)
    bsData = bs1.findAll('tr')
    print(bsData)
    canidateNames = []
    canidateParties = []
    for i in range(len(bsData)-2):
        canid = list(bsData[i+2].children)
        # print(candid)
        canidateNames.append(canid[7].getText().strip())
        canidateParties.append(canid[3].getText().strip())
    #
    tableContents = bsObj.find("table", { "class" : "elections_states" })
    list = []
    count1 = 0
    state = "state"
    candidate_name = "cname"
    party = "party"
    popular_vote = "pv"
    electoral_votes = "ev"
    print("******"+year+"******")
    for thing in tableContents:
        count2 = 0
        for item in thing:
            if count1 != 0:
                if str(item).strip() != "":
                    
                    item = str(item)
                    if "span" in item:
                        span = item.find("span")
                        item = item[span:]
                    if "<p " in item:
                        p = item.find("<p ")
                        item = item[p:]
                    if "<font " in item:
                        font = item.find("<font ")
                        item = item[font:]
                    start = item.find(">")
                    end = item[start:].find("<")
                    newItem = item[start+1:start+end]
                    if newItem.strip() != "":
                        # print("*"+item+"*"+newItem+"*")
                        match = re.search('([A-Z a-z]+)', newItem)
                        if match != None:
                            if match.group(0) != "Votes":
                                state = match.group(0)

                        if count2 == 2:
                            popular_vote = newItem
                        # print(canidateNames)
                        if count2 == 4:
                            electoral_votes = newItem
                            try:
                                if int(newItem) > 1000:
                                    electoral_votes = 0
                            except ValueError:
                                electoral_votes = 0
                        count2 += 1
                        
            else:
                count1 += 1

        if state != "state" and state != "Totals" and state != "Total" and state != "States" and state != "" and state != "EV" and state[0] != " " :
            if state not in list:
                printFile(year, state, candidate_name, party, popular_vote, electoral_votes)
                list.append(state)

       
    # f = open("year"+year, "w")
    # print(thing)
    # print(thing, file=f)
    # f.close()


def printFile(year, state, candidate_name, party, popular_vote, electoral_votes):
    f = open("data", "a")
    print(year, state, candidate_name, party, popular_vote, electoral_votes, file=f)
    f.close()


def years():
    for i in range(0, 20):
        year = i*4+1940
        presidents(str(year))
        if year == 2012:
            break

years()
