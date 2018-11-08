from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
author_id=input("Input the Author ID you want to process: ")
#Give Author ID as 15841421100 for test
url="https://www.scopus.com/authid/detail.uri?authorId="+str(author_id)
os.chdir(r'C:\Users\rgoulika\Downloads')
# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
cit=driver.find_element_by_id("totalCiteCount")
sub=driver.find_element_by_id("subjectAreaBadges")
d1=driver.find_element_by_class_name("resultsCountDoc")
d=driver.find_element_by_class_name("resultsCountCite")
d2=driver.find_element_by_id('coAuthLi')
print(d.text)
print(d1.text)
print(d2.text.strip("co-authors"))
driver.close()
