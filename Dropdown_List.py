from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select")

var = Select(driver.find_element(By.ID, "pet-select"))
# <select name="pets" id="pet-select">

#select_by_visible_text
var.select_by_visible_text("Cat")
time.sleep(2)

#select_by_value
#select_by_index

driver.quit()