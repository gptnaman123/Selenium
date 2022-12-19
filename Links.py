# For automated finding and clicking of links, present on a website.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")

links = driver.find_elements(By.TAG_NAME, "a") #find all links(anchor tags)
print(len(links))

# for link in links:
#     print(link.text)  #to print all link texts present on the website

driver.find_element(By.LINK_TEXT, 'Software Testing Tutorials').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Tutorials").click()


driver.quit()








