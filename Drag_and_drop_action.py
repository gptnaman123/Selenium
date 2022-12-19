from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(2)

action = ActionChains(driver)

source = driver.find_element(By.ID, "draggable")
#<div id="draggable" class="ui-widget-content ui-draggable ui-draggable-handle" style="position: relative;">
target = driver.find_element(By.ID, "droppable")
#<div id="droppable" class="ui-widget-header ui-droppable">

action.drag_and_drop(source,target).perform()

time.sleep(3)

print("OK")
driver.quit()