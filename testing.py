import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.naukri.com/information-technology-jobs?xt=catsrch&qf[]=24'
#'https://www.naukri.com/top-jobs-by-designations#'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_divs = soup.find('div',{'id':'nameSearch'})

count = 0
for job_profile in job_profiles:
	print(job_profile.text)
	count = count + 1
	if(count == 10):
		break
driver.close()