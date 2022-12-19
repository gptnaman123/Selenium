from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame") #use the name element in frame tag
#<iframe src="overview-frame.html" name="packageListFrame" title="All Packages"></iframe>
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
#<iframe src="allclasses-frame.html" name="packageFrame" title="All classes and interfaces (except non-static nested types)"></iframe>
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/iframe")
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
#<iframe src="overview-summary.html" name="classFrame" title="Package, class and interface descriptions" class="rightIframe"></iframe>
driver.find_element(By.LINK_TEXT, "accept()").click()

driver.quit()