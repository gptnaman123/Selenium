from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

print("OK")
driver.quit()