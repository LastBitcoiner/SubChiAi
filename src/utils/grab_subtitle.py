from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time

PATH = r"C:\Users\omido\Documents\GitHub\SubChiAI\SubChiAi\bin\chromedriver.exe"
DL_PATH = r"C:\Users\omido\Documents\GitHub\SubChiAI\SubChiAi\src\assets\subs"


def grab_sub(vid_link, selenium_path=0, download_path=0):

    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": DL_PATH,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    options.add_argument('log-level=3')

    driver = webdriver.Chrome(PATH, options=options)

    link_payload = "https://savesubs.com/process?url="+vid_link
    driver.get(link_payload)
    time.sleep(10)

    sublink = driver.find_element_by_xpath(
        "(//a[contains(@class,'w-4/12 mx-1')])[3]")
    sublink.get_attribute("href")
    sublink.click()
    time.sleep(5)
