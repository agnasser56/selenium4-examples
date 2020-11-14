

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
driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 412,
        "height": 892,
        "deviceScaleFactor": 0,
        "mobile": True
})

driver.get("https://www.google.com/")

time.sleep(3)
    
txtLocation = driver.find_element_by_name("q")
time.sleep(3)
txtLocation.send_keys("Chicago")
txtLocation.send_keys(Keys.RETURN)
print("Device Emulation with Selenium 4 is complete")
