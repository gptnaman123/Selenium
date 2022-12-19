from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
#<button class="btn btn-info">    click   </button>
print(driver.current_window_handle) # prints Hexadecimal value of current/parent window

handles = driver.window_handles #child window

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

    if driver.title == "Frames & windows":
        driver.close() #close parent window

print("OK")
driver.quit()


