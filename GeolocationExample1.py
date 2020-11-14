

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
import urllib3
import warnings

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

s = Service("ChromeDriver\chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": 42.1408845,
        "longitude": -72.5033907,
        "accuracy": 100
})

driver.get("https://locations.dennys.com/search.html/")

time.sleep(10)
    
location_icon = driver.find_element_by_css_selector(".icon-geolocate")
time.sleep(10)
location_icon.click()

time.sleep(10)
print("Geolocation testing with Selenium is complete")
