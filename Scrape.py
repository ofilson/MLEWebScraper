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

season = soup.find('div', attrs={'id':'elementor-tab-title-2413'}) # Season 8

b = soup.find('div', attrs={'aria-labelledby':'elementor-tab-title-2413'}) #Season 8

c = b.findNext('div', attrs={'class':'sp-template-event-list'})
print(c.findNext('h4').text)