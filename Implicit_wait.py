'''
An implicit wait is a global wait applied to all the elements on the page. The wait time is provided as arguments
to the method. For example, if the wait time is 5 seconds, it shall wait this period of time before throwing a
timeout exception.

An implicit wait is a dynamic wait which means if the element is available at the third second, then we shall move
to the next step of the test case instead of waiting for the entire five seconds.

An implicit wait informs the web driver to poll for a specific amount of time. Once this time is determined, it
remains for the entire driver session. The default time of an implicit wait is 0.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial")
myDynamicElement = driver.find_element(By.CLASS_NAME ,"header-main__container")
print("Ok")

driver.quit()