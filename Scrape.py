#imports
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

# Here we will grab the URL's to each match throughout the season, and then we will grab from those URLs (maybe in a different scraper?)

driver = webdriver.Chrome("C:/Users/Oscar Filson/eclipse-workspace/MLEWebScraper/MLEWebScraper/chromedriver")

matchLinks=[] #list the links to the data on each match
driver.get("https://mlesports.gg/matches/") # URL to scrape from: https://mlesports.gg/matches/

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")

#Comment one of these out
#seasonIDs = ['2413']                #For testing using just one season (season 8)
seasonIDs = ['2413','2412','2411']  #For testing using all three seasons (8-10)

for a in seasonIDs:
    season = soup.find('div', attrs={'id':'elementor-tab-title-'+a}).text # Season number (ie Season 8)
    print(season)
    seasonData = soup.find('div', attrs={'aria-labelledby':'elementor-tab-title-'+a}) 
    for leagueData in seasonData.findAll('div', attrs={'class':'sp-template-event-list'}):
        League = leagueData.findNext('h4').text
        print(League)