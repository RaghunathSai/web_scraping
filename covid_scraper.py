import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import requests
from requests import get

url = 'https://www.mohfw.gov.in/'
results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

active = []
cured = []
deaths = []
migrated = []
Date = []

covid_div = soup.find_all('div',class_='site-stats-count')

for count in covid_div:
    
    #count of active cases in india
    active_count = count.ul.find('li',class_='bg-blue').strong.text if(count.ul.find('li',class_='bg-blue').strong.text) else '-'
    active.append(active_count)
   
    #count of cured/discharged cases
    dead_count = count.ul.find('li',class_='bg-red').strong.text if(count.ul.find('li',class_='bg-red').strong.text) else '-'
    deaths.append(dead_count)

    #count of cured cases
    cured_count = count.ul.find('li',class_='bg-green').strong.text if(count.ul.find('li',class_='bg-green').strong.text) else '-'
    cured.append(cured_count)

    #count of migrant cases
    migrant_count = count.ul.find('li',class_='bg-orange').strong.text if(count.ul.find('li',class_='bg-orange').strong.text) else '-'
    migrated.append(migrant_count)

    #date details
    date_value = count.find('div',class_='status-update').find('span').text if(count.find('div',class_='status-update').find('span').text) else '-'
    date_value = date_value.lstrip('as on  :').rstrip('(GMT+5:30)')
    Date.append(date_value)

#building the pandas dataframe
covid_cases = pd.DataFrame({
'Date':Date,
'Active':active,
'Dead':deaths,
'Cured':cured,
"Migrated":migrated,
})
print(covid_cases)