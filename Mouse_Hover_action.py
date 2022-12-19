from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.edureka.co/")

action = ActionChains(driver)
menu = driver.find_element(By.XPATH, "/html/body/nav/div[1]/a/span/b")
action.move_to_element(menu).perform() #mouse hovering action performed

sub_menu = driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[3]/a")
sub_menu.click()

time.sleep(4)

print("OK")
driver.quit()

