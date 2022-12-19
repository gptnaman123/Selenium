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

driver.save_screenshot("test1_ss.png")
#get_screenshot_as_file
#get_screenshot_as_png
#get_screenshot_as_base64

time.sleep(3)

driver.quit()