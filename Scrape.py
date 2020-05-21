# author - Chef Filson
# date - 5/19/2020

#imports
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import pandas as pd 

#This makes a simple function to call when parsing data using BeautifulSoup and Selenium. Gets rid of error as well.
def makeSoup(seleniumObject):
    return BeautifulSoup(seleniumObject.get_attribute('innerHTML'), features='lxml')

# ----------------------------------------------------
#                 "Matches" parser
# ----------------------------------------------------

driver = webdriver.Chrome("C:/Users/Oscar Filson/eclipse-workspace/MLEWebScraper/MLEWebScraper/chromedriver")
driver.get("https://mlesports.gg/matches/") # scrapes from this URL

#This works
testButton = driver.find_element_by_xpath('/html/body/div[2]/header/div/div/div/div[2]/nav/div/ul/li[5]/a')
#actionChains.move_to_element(testButton)
#actionChains.click()
#actionChains.perform()

#Comment one of these out
#seasonIDs = ['2413']                 #For testing using just one season (season 8)
#tableNumber = 12
seasonIDs = ['2411','2412','2413']  #For testing using all three seasons (10-8)
tableNumber = 0

for a in seasonIDs:

    season = driver.find_element_by_id('elementor-tab-title-'+a) # Season number (ie Season 8)
    seasonSoup = makeSoup(season)
    print('Processing ' + seasonSoup.text)

    seasonData = driver.find_element_by_id('elementor-tab-content-'+a)
    seasonDataSoup = makeSoup(seasonData)
#    print(seasonDataSoup)

    leagues = []

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
#            print(nextButtonSoup)
            try: #Tries to find a disabled pagination button, throws a NoSuchElement if not first or last page
                disabledSoup = makeSoup(leagueData.find_element_by_class_name('disabled')) 
            except:
                disabledSoup = None
#            print(disabledSoup)
            if disabledSoup == nextButtonSoup:  #if statement that figures out if the next button exists: True if it does, False if it doesn't
                buttonExists = False

            actionChains.move_to_element(nextButton)
            actionChains.click()

            for row in leagueData.find_elements_by_class_name('sp-row'):

                resultData = row.find_element_by_class_name('data-time')
                resultDataSoup = makeSoup(resultData)
#               print(resultDataSoup)

                link = resultDataSoup.find('a').get('href')
#                print(link)
                urls.append(link)
            if buttonExists:         
                actionChains.perform() #Go to next page
        tableNumber = tableNumber + 1
        leagues.append(urls)
        urls = []
        print(league + ' has been processed')
    print(seasonSoup.text + ' has been processed')
    #go into seperate function passing in leagues that 

print('Done!')