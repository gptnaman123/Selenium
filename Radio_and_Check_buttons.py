from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_forms.asp")

'''Radio button click'''
var = driver.find_element(By.ID, "html")
# <input type="radio" id="html" name="fav_language" value="HTML">
var.click()
time.sleep(2)

'''2 Check buttons click'''
var1 = driver.find_element(By.ID, "vehicle1")
# <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
var1.click()
time.sleep(2)

var2 = driver.find_element(By.ID, "vehicle2")
# <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
var2.click()
time.sleep(2)

print("OK")
driver.quit()
