from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe") #driver variable used to run all commands
driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial") #get is used to open the website

#web driver commands
print(driver.title)
driver.maximize_window()
driver.minimize_window()
driver.quit()