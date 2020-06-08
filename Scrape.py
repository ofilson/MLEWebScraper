# author - Chef Filson
# date - 5/19/2020

#imports
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import pandas as pd 
import csv
import re

#This makes a simple function to call when parsing data using BeautifulSoup and Selenium. Gets rid of error as well.
def makeSoup(seleniumObject):
    return BeautifulSoup(seleniumObject.get_attribute('innerHTML'), features='lxml')

def removeWhiteSpace(string):
    return re.sub(r"\s+", "", string)

# ----------------------------------------------------
#                 Match parser
# ----------------------------------------------------

def getMatchData(url, league, season):
    driver = webdriver.Chrome("C:/Users/Oscar Filson/eclipse-workspace/MLEWebScraper/chromedriver")
    driver.get(url)
    ## Make Variables
    t1Name = t1Wins = t1p1Name = t1p2Name = ''
    week = t1p1Salary = t1p1Goals = t1p1Assists = t1p1Saves = t1p1Shots = t1p2Salary = t1p2Goals = t1p2Assists = t1p2Saves = t1p2Shots = 0
    t2Name = t2Wins = t2p1Name = t2p2Name =  ''
    t2p1Salary = t2p1Goals = t2p1Assists = t2p1Saves = t2p1Shots = t2p2Salary = t2p2Goals = t2p2Assists = t2p2Saves = t2p2Shots = 0
    ## Get Week
    matchData = driver.find_element_by_id('primary') 
    detailsTable = matchData.find_element_by_class_name('sp-section-content-details')
    detailsData = detailsTable.find_elements_by_tag_name('tr')[1]
    weekRaw = detailsData.find_elements_by_tag_name('td')[4]
    weekSoup = makeSoup(weekRaw)
    week = weekSoup.text
    ## Get Name and wins for both teams
    matchesTable = matchData.find_element_by_class_name('sp-section-content-results')
    matchesData = matchesTable.find_elements_by_tag_name('tr')
    t1Data = matchesData[1].find_elements_by_tag_name('td')
    t1Name = makeSoup(t1Data[0]).text
    t1Wins = makeSoup(t1Data[1]).text
    t2Data = matchesData[2].find_elements_by_tag_name('td')
    t2Name = makeSoup(t2Data[0]).text
    t2Wins = makeSoup(t2Data[1]).text
    # Get Team One Player One data
    teamTables = matchData.find_elements_by_class_name('sp-template-event-performance-values')
    t1Table = teamTables[0].find_element_by_tag_name('tbody')
    p1Row = t1Table.find_element_by_tag_name('tr')
    p1Data = p1Row.find_elements_by_tag_name('td')
    t1p1Name = makeSoup(p1Data[0]).text
    t1p1Goals = makeSoup(p1Data[1]).text
    t1p1Assists = makeSoup(p1Data[2]).text
    t1p1Saves = makeSoup(p1Data[3]).text
    t1p1Shots = makeSoup(p1Data[4]).text
    #Get Team One Player Two data
    p2Row = t1Table.find_elements_by_tag_name('tr')[1]
    p2Data = p2Row.find_elements_by_tag_name('td')
    t1p2Name = makeSoup(p2Data[0]).text
    t1p2Goals = makeSoup(p2Data[1]).text
    t1p2Assists = makeSoup(p2Data[2]).text
    t1p2Saves = makeSoup(p2Data[3]).text
    t1p2Shots = makeSoup(p2Data[4]).text
    #Get Team Two Player One data
    t2Table = teamTables[1].find_element_by_tag_name('tbody')
    p1Row = t2Table.find_element_by_tag_name('tr')
    p1Data = p1Row.find_elements_by_tag_name('td')
    t2p1Name = makeSoup(p1Data[0]).text
    t2p1Goals = makeSoup(p1Data[1]).text
    t2p1Assists = makeSoup(p1Data[2]).text
    t2p1Saves = makeSoup(p1Data[3]).text
    t2p1Shots = makeSoup(p1Data[4]).text
    #Get Team Two Player Two data
    p2Row = t2Table.find_elements_by_tag_name('tr')[1]
    p2Data = p2Row.find_elements_by_tag_name('td')
    t2p2Name = makeSoup(p2Data[0]).text
    t2p2Goals = makeSoup(p2Data[1]).text
    t2p2Assists = makeSoup(p2Data[2]).text
    t2p2Saves = makeSoup(p2Data[3]).text
    t2p2Shots = makeSoup(p2Data[4]).text
    # Write to .csv
    csvName = removeWhiteSpace(season) + removeWhiteSpace(league) + '.csv'
    with open(csvName, 'a') as test:
        testWriter = csv.writer(test, delimiter = ',', lineterminator = '\n')

        testWriter.writerow([week, t1Name, t1Wins, t1p1Name, t1p1Goals, t1p1Assists, t1p1Saves, t1p1Shots, t1p2Name, t1p2Goals, t1p2Assists, t1p2Saves, t1p2Shots, 
        t2Name, t2Wins, t2p1Name, t2p1Goals, t2p1Assists, t2p1Saves, t2p1Shots, t2p2Name, t2p2Goals, t2p2Assists, t2p2Saves, t2p2Shots])

    driver.close()
# ----------------------------------------------------
#                 Schedule parser
# ----------------------------------------------------

driver = webdriver.Chrome("C:/Users/Oscar Filson/eclipse-workspace/MLEWebScraper/chromedriver")
driver.get("https://mlesports.gg/matches/") # scrapes from this URL

#Comment one of these out
#seasonIDs = ['2413']                 #For testing using just one season (season 8)
#tableNumber = 12
seasonIDs = ['2411','2412','2413']  #For using all three seasons (10-8)
tableNumber = 0

for a in seasonIDs:

    season = driver.find_element_by_id('elementor-tab-title-'+a) # Season number (ie Season 8)
    seasonSoup = makeSoup(season)
    print('Processing ' + seasonSoup.text)

    seasonData = driver.find_element_by_id('elementor-tab-content-'+a)
    seasonDataSoup = makeSoup(seasonData)

#   leagues = []

    tabNum = a[3]
    correctTab = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/main/article/div/div/div/div/section/div/div/div/div/div/div/div/div/div[1]/div['+ tabNum + ']/a')
    actionChains = ActionChains(driver)
    actionChains.move_to_element(correctTab)
    actionChains.click().perform()
    
    for leagueData in seasonData.find_elements_by_class_name('sp-template-event-list'):

        leagueName = leagueData.find_element_by_tag_name('h4')
        leagueNameSoup = makeSoup(leagueName)
        league = leagueNameSoup.text[0:leagueNameSoup.text.index('League')+6]
        print('Processing ' + league)
        urls = []

        buttonExists = True
        
        while(buttonExists):
            actionChains = ActionChains(driver) # Must be re-instantiated every iteration or else element becomes stale
            if(tableNumber == 8):
                tableNumber += 4 #Account for weird playoff data in season 8
            tableNum = tableNumber.__str__()
            nextButton = leagueData.find_element_by_xpath('//*[@id="DataTables_Table_' + tableNum + '_next"]')
            
            nextButtonSoup = makeSoup(nextButton)
            try: #Tries to find a disabled pagination button, throws a NoSuchElement if not first or last page
                disabledSoup = makeSoup(leagueData.find_element_by_class_name('disabled')) 
            except:
                disabledSoup = None
            if disabledSoup == nextButtonSoup:  #if statement that figures out if the next button exists: True if it does, False if it doesn't
                buttonExists = False

            actionChains.move_to_element(nextButton)
            actionChains.click()
            for row in leagueData.find_elements_by_class_name('sp-row'):
                resultData = row.find_element_by_class_name('data-time')
                resultDataSoup = makeSoup(resultData)

                link = resultDataSoup.find('a').get('href')
                urls.append(link)
            if buttonExists:         
                actionChains.perform() #Go to next page
        tableNumber = tableNumber + 1
#        leagues.append(urls)
        for url in urls:
            getMatchData(url, league, seasonSoup.text)
        urls = []
        print(league + ' has been processed')
    print(seasonSoup.text + ' has been processed')
    #go into seperate function passing in leagues that 

driver.close()
print('Done!')