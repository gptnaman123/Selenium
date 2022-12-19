'''
Selenium: For browser automation, it is a framework to program automation softwares.

Selenium Web Driver: Selenium Webdriver is the parent of all methods and classes used in Selenium Python.
It is the driving force of Selenium that allows us to perform various operations on multiple elements on a webpage.
Driver has various methods and attributes one can use to automate testing in Selenium Python.
'''


from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe") #driver variable used to run all commands
driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial") #get is used to open the website





