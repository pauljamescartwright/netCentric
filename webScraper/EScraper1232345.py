
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



def readNameTable(url):
    html= urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    element = bs.findAll("table", {"class":"elections_states"})
    
    try:
        nameTable = element[1] 
    except IndexError:
        nameTable = element

    bsData = nameTable.findAll('tr')
    canidateNames = []
    canidateParties = []

    for i in range(len(bsData)-2):
        canid = list(bsData[i+2].children)
        canidateNames.append(canid[7].getText().strip())
        canidateParties.append(canid[3].getText().strip())

    presidents(url, canidateNames, canidateParties)


def presidents(url, canidateNames, canidateParties):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")

    tableContents = bsObj.find("table", { "class" : "elections_states" }) ######looping over each year
    list = []
    count1 = 0
    state = "state"
    year = "1940"
    candidate_name = canidateNames[0]
    candidate_name1 = canidateNames[1]
    try:
        candidate_name2 = canidateNames[2]
    except IndexError:
        hello = "sup"
    party = canidateParties[0]
    popular_vote = "pv"
    electoral_votes = "ev"
    popular_vote1 = "pv1"
    electoral_votes1 = "ev1"
    popular_vote2 = "pv2"
    electoral_votes2 = "ev2"
    print("******"+year+"******")
    for thing in tableContents:   #######looping over each year
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
                        if count2 == 4:
                            electoral_votes = newItem
                            try:
                                if int(newItem) > 1000:
                                    electoral_votes = 0
                            except ValueError:
                                electoral_votes = 0

                        if count2 == 5:
                            popular_vote = newItem
                        if count2 == 7:
                            electoral_votes = newItem
                            try:
                                if int(newItem) > 1000:
                                    electoral_votes = 0
                            except ValueError:
                                electoral_votes = 0
                        try: 
                            if count2 == 8:
                                popular_vote = newItem
                            if count2 == 10:
                                electoral_votes = newItem
                                try:
                                    if int(newItem) > 1000:
                                        electoral_votes = 0
                                except ValueError:
                                    electoral_votes = 0
                        except IndexError:
                            onlyTwoDudes = True




                        count2 += 1
                        
            else:
                count1 += 1

        if state != "state" and state != "Totals" and state != "Total" and state != "States" and state != "" and state != "EV" and state[0] != " " :
            if state not in list:
                #print(year, state, candidate_name, party, popular_vote, electoral_votes)
                printFile(year, state, candidate_name, candidate_name1, candidate_name2, party, popular_vote, popular_vote1, popular_vote2, electoral_votes, electoral_votes1, electoral_votes2) ##prints stuff here
                list.append(state)




def printFile(year, state, candidate_name, candidate_name1, candidate_name2, party, popular_vote, popular_vote1, popular_vote2, electoral_votes, electoral_votes1, electoral_votes2): ##prints stuff
    f = open("ElectionScrape.txt", "a")
    print(year, state, candidate_name, party, popular_vote, electoral_votes, file=f)
    print(year, state, candidate_name1, party, popular_vote1, electoral_votes1, file=f)
    print(year, state, candidate_name2, party, popular_vote2, electoral_votes2, file=f)
    f.close()


#def years(): ################## sends year to main function     
 #       presidents(str(1952))

readNameTable("http://www.presidency.ucsb.edu/showelection.php?year=1948")


#years()
