from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://masterprograming.com")

time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)", "") #scrolls down from 0 to 1000 px
time.sleep(3)

print("OK")
driver.quit()