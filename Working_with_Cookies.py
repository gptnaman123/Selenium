from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial/")

cookies = driver.get_cookies()

for cookie in cookies:
    print(cookie)

time.sleep(4)
driver.quit()