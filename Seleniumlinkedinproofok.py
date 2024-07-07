#!/usr/bin/env python
# coding: utf-8

# In[389]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import pandas as pd
import time


# In[391]:


# Configure Chrome options
options = Options()
options.add_argument('--headless')  # Optional: run Chrome in headless mode


# In[393]:


url1 = 'https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analys&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'


# In[395]:


# Specify the path to the ChromeDriver executable
chromedriver_path = r'C:\chromedriver-win32\chromedriver-win32\chromedriver.exe'
# Initialize Chrome WebDriver with the specified executable path
driver = webdriver.Chrome(service=Service(executable_path=chromedriver_path))
driver.get(url1)
driver.implicitly_wait(10)


# In[387]:


n = driver.find_elements(By.CLASS_NAME,'results-context-header__job-count')[0].text
n
y=pd.to_numeric(n)
y


# In[397]:


i=2
while i<=26:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i=i+1

    try:
        x = driver.find_element(By.XPATH, "//button[@aria-label='See more jobs']")
        driver.execute_script("arguments[0].click();",x)
        time.sleep(6)
    except:
        pass
        time.sleep(7)


# In[398]:


companyname=[]
titlename=[]
for j in range(y):
    try:
        company=driver.find_elements(By.CLASS_NAME,'base-search-card__title')[j].text
        companyname.append(company)


    except IndexError:
 #       print("done")
        pass
for k in range(y):
    try:

        title=driver.find_elements(By.CLASS_NAME,'base-search-card__subtitle')[k].text
        titlename.append(title)

    except IndexError:
 #       print("done")
        pass


# In[401]:


companyname[0]
titlename[0]


# In[403]:


companyfinal=pd.DataFrame(companyname,columns=["company"])


# In[529]:


titlefinal=pd.DataFrame(titlename,columns=["title"])


# In[535]:


final=companyfinal.join(titlefinal)
final.to_csv('linkedinjobdetails.csv')


# In[531]:


linklist= []
findlink=driver.find_elements(By.CLASS_NAME,'base-card__full-link')
for k in findlink:
    linklist.append(k.get_attribute('href'))
linklistfinal=pd.DataFrame(findlink,columns=["linklist"])


# In[ ]:







