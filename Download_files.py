from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.selenium.dev/downloads/")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[2]/div/div/p[1]/a").click()
#<a href="https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.7.0/selenium-server-4.7.2.jar">4.7.2</a>

time.sleep(10)

driver.quit()