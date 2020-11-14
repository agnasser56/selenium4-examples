

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
        "latitude": 30.051744, 
        "longitude": 31.235115,
        "accuracy": 100
})

driver.get("https://www.google.com/")

time.sleep(3)
location_icon = driver.find_element_by_name("q")

location_icon.send_keys("pizza hut")
time.sleep(3)

location_icon.send_keys(Keys.RETURN)

lnkMaps = driver.find_element_by_xpath("//a[text()='Maps']")
lnkMaps.click()

print("Geolocation testing with Selenium is complete")
