from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://google.com")
print(driver.title)
time.sleep(2)

driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial")
print(driver.title)
time.sleep(2)

driver.back()  #goes back to google.com
print(driver.title)
driver.forward()   #goes forward to gfg website
print(driver.title)

driver.quit()