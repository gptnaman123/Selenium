from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")

action = ActionChains(driver)

select = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
action.double_click(select).perform()

time.sleep(3)

print("OK")
driver.quit()