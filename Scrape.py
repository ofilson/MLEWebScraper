# author - Chef Filson
# date - 5/19/2020

#imports
from selenium import webdriver
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

#Comment one of these out
seasonIDs = ['2413']                #For testing using just one season (season 8)
#seasonIDs = ['2413','2412','2411']  #For testing using all three seasons (8-10)

for a in seasonIDs:
    season = driver.find_element_by_id('elementor-tab-title-'+a) # Season number (ie Season 8)
    seasonSoup = makeSoup(season).text #Season 8
#   print(seasonSoup)
#   seasonData = soup.find('div', attrs={'aria-labelledby':'elementor-tab-title-'+a}) 
    seasonData = driver.find_element_by_id('elementor-tab-content-'+a)
    seasonDataSoup = makeSoup(seasonData)
    print(seasonDataSoup)
    break
    for leagueData in seasonData.findAll('div', attrs={'class':'sp-template-event-list'}):
        League = leagueData.findNext('h4').text
        print(League)
        
        for row in leagueData.findAll('tr'):
            result = row.find('td', attrs={'class':'data-time ok'})
            print(result)

        print(leagueData)
        nextButton = leagueData.findNext('a', attrs={'class':'next'})
        print(nextButton)
        
        #I need to figure out a way to click the next button on selenium I think.