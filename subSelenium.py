#!/usr/bin/env python
# coding: utf-8

# In[44]:


#use selenium to download subtitles
#imports :
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time


# In[45]:


PATH = r"C:\Users\omido\Documents\GitHub\SubChiAI\bin\chromedriver.exe"


options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\omido\Documents\GitHub\SubChiAI\Subs",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


driver = webdriver.Chrome(PATH,options=options)


# In[46]:


driver.get("https://savesubs.com/process?url=https://www.youtube.com/watch?v=fbmRTIke2mQ")
time.sleep(3)


# In[47]:


sublink = driver.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div[1]/ul/li[2]/section/a[2]')
sublink.get_attribute("href")
sublink.click()


# In[ ]:




