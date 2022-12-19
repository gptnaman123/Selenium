from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Wiki")

var = driver.find_element(By.CLASS_NAME, "vector-search-box-input")
print(var.is_displayed())  #tells whether search box is displayed or not

var2 = driver.find_element(By.NAME, "search")
print(var.is_enabled())  #tells whether search box is enabled for typing or not

var3 = driver.find_element(By.NAME, "search")
print(var.is_selected())  #tells whether a radio/check button is selected or not

driver.quit()


'''
<input class="vector-search-box-input" type="search" name="search" placeholder="Search Wikipedia" 
aria-label="Search Wikipedia" autocapitalize="sentences" title="Search Wikipedia [alt-shift-f]" 
accesskey="f" id="searchInput" autocomplete="off">
'''