# this file is to test the match scraper on an individual match before putting it in the main scraper.
# author - Chef Filson
# date - 5/19/2020

#imports
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import pandas as pd 
import csv

def makeSoup(seleniumObject):
    return BeautifulSoup(seleniumObject.get_attribute('innerHTML'), features='lxml')

driver = webdriver.Chrome("C:/Users/Oscar Filson/eclipse-workspace/MLEWebScraper/chromedriver")
driver.get("https://mlesports.gg/event/4918/") # scrapes from this URL

#data I need:
week = 0
t1Name = t1Wins = t1p1Name = ''
t1p1Salary = t1p1Goals = t1p1Assists = t1p1Saves = t1p1Shots = 0
t1p2Name = ''
t1p2Salary = t1p2Goals = t1p2Assists = t1p2Saves = t1p2Shots = 0

t2Name = t2Wins = t2p1Name = ''
t2p1Salary = t2p1Goals = t2p1Assists = t2p1Saves = t2p1Shots = 0
t2p2Name = ''
t2p2Salary = t2p2Goals = t2p2Assists = t2p2Saves = t2p2Shots = 0

matchData = driver.find_element_by_id('primary') 
detailsTable = matchData.find_element_by_class_name('sp-section-content-details')
detailsData = detailsTable.find_elements_by_tag_name('tr')[1]
weekRaw = detailsData.find_elements_by_tag_name('td')[4]
weekSoup = makeSoup(weekRaw)
week = weekSoup.text
print('Week = ' + week)

matchesTable = matchData.find_element_by_class_name('sp-section-content-results')
matchesData = matchesTable.find_elements_by_tag_name('tr')
t1Data = matchesData[1].find_elements_by_tag_name('td')
t1Name = makeSoup(t1Data[0]).text
t1Wins = makeSoup(t1Data[1]).text
t2Data = matchesData[2].find_elements_by_tag_name('td')
t2Name = makeSoup(t2Data[0]).text
t2Wins = makeSoup(t2Data[1]).text
print('t1 = ' + t1Name)
print('t1 wins = ' + t1Wins)
print('t2 = ' + t2Name)
print('t2 wins = ' + t2Wins)

teamTables = matchData.find_elements_by_class_name('sp-template-event-performance-values')
t1Table = teamTables[0].find_element_by_tag_name('tbody')
p1Row = t1Table.find_element_by_tag_name('tr')
p1Data = p1Row.find_elements_by_tag_name('td')
t1p1Name = makeSoup(p1Data[0]).text
t1p1Goals = makeSoup(p1Data[1]).text
t1p1Assists = makeSoup(p1Data[2]).text
t1p1Saves = makeSoup(p1Data[3]).text
t1p1Shots = makeSoup(p1Data[4]).text
print(t1p1Name + ", " + t1p1Goals + ", " + t1p1Assists + ", " + t1p1Saves + ", " + t1p1Shots)

p2Row = t1Table.find_elements_by_tag_name('tr')[1]
p2Data = p2Row.find_elements_by_tag_name('td')
t1p2Name = makeSoup(p2Data[0]).text
t1p2Goals = makeSoup(p2Data[1]).text
t1p2Assists = makeSoup(p2Data[2]).text
t1p2Saves = makeSoup(p2Data[3]).text
t1p2Shots = makeSoup(p2Data[4]).text
print(t1p2Name + ", " + t1p2Goals + ", " + t1p2Assists + ", " + t1p2Saves + ", " + t1p2Shots)

t2Table = teamTables[1].find_element_by_tag_name('tbody')
p1Row = t2Table.find_element_by_tag_name('tr')
p1Data = p1Row.find_elements_by_tag_name('td')
t2p1Name = makeSoup(p1Data[0]).text
t2p1Goals = makeSoup(p1Data[1]).text
t2p1Assists = makeSoup(p1Data[2]).text
t2p1Saves = makeSoup(p1Data[3]).text
t2p1Shots = makeSoup(p1Data[4]).text
print(t2p1Name + ", " + t2p1Goals + ", " + t2p1Assists + ", " + t2p1Saves + ", " + t2p1Shots)

p2Row = t2Table.find_elements_by_tag_name('tr')[1]
p2Data = p2Row.find_elements_by_tag_name('td')
t2p2Name = makeSoup(p2Data[0]).text
t2p2Goals = makeSoup(p2Data[1]).text
t2p2Assists = makeSoup(p2Data[2]).text
t2p2Saves = makeSoup(p2Data[3]).text
t2p2Shots = makeSoup(p2Data[4]).text
print(t2p2Name + ", " + t2p2Goals + ", " + t2p2Assists + ", " + t2p2Saves + ", " + t2p2Shots)

with open('test.csv', 'a') as test:
    testWriter = csv.writer(test, delimiter = ',', lineterminator = '\n')

    testWriter.writerow([week, t1Name, t1Wins, t1p1Name, t1p1Goals, t1p1Assists, t1p1Saves, t1p1Shots, t1p2Name, t1p2Goals, t1p2Assists, t1p2Saves, t1p2Shots, 
    t2Name, t2Wins, t2p1Name, t2p1Goals, t2p1Assists, t2p1Saves, t2p1Shots, t2p2Name, t2p2Goals, t2p2Assists, t2p2Saves, t2p2Shots])