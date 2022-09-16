"""
Richard Mayers July 7th, 2022
"""


from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


#comparator variables used later on
commonString = "<img alt=\"\" class=\"banner\" data-v-e040963e=\"\" src=\"/img/banner.eed41ef6.png\"/>"
uncommonString="<img alt=\"\" class=\"banner\" data-v-e040963e=\"\" src=\"/img/banner.4cbe1985.png\"/>"
rareString="<img alt=\"\" class=\"banner\" data-v-e040963e=\"\" src=\"/img/banner.cc4653d7.png\"/>"

#variable creation
cardID = []
cardRarity = []
cardType = []
cardName = []
energyCost = []
cardDescription = []

#create driver object
driver = webdriver.Chrome()

# causes data pulled to be in English
headers = {"Accept-Language": "en-US, en;q=0.5"}

# URL of website stored in variable
url = "https://maybelatergames.co.uk/tools/slaythespire/"

# URL's informations stored in seperate variable
driver.get(url)

#BeautifulSoup used to turn URL info into easily readable information

soup = BeautifulSoup(driver.page_source, 'html.parser')  #seperates URL data into seperate components

#create List to grab all cards' relevant tags
idList = []

for i in range(75):
    idList.append(str("card-" + str(i)))
    
    
#finding the div IDs that have the data we want
card_div = soup.find_all(id=idList)
idList.clear()

   
loopNum = 0
#for loop to run through every card
for container in card_div:
    cardID.append(loopNum)
    if(str(container.find('img',class_='banner')) == commonString):
        cardRarity.append('Common')
    elif(str(container.find('img',class_='banner')) == uncommonString):
        cardRarity.append('Uncommon')
    else:
        cardRarity.append('Rare')
    if(str(container.find('p',class_='type')).__contains__("attack")):
        cardType.append('Attack')
    elif(str(container.find('p',class_='type')).__contains__("skill")):
        cardType.append('Skill')
    elif(str(container.find('p',class_='type')).__contains__("power")):
        cardType.append('Power')
    else:
        cardType.append('Curse')
    cardName.append(container.find('p',class_='title').text.strip())
    try:
        energyCost.append(container.find('p',class_='mana-text').text.strip())
    except:
        energyCost.append("None")
    cardDescription.append(container.find('div',class_='description').text.strip())
    loopNum +=1

    
for ID in cardID:
    print(str(f"{{{cardID[ID]},new Card( {cardID[ID]},\"{cardName[ID]}\",\"{cardType[ID]}\",\"{cardRarity[ID]}\",\"{energyCost[ID]}\", \"{cardDescription[ID]}\")}},")) 
