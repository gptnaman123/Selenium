'''
Automated filling of input and text boxes on a website(for example, reviews aur contact us section)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.cyiai.com")

name = driver.find_element(By.NAME, "name")
#<input name="name" type="text" class="form-control" id="name" placeholder="Full Name" required="">
name.send_keys("Naman Gupta")
time.sleep(2)

email = driver.find_element(By.NAME, "email")
#<input name="email" type="email" class="form-control" id="email" placeholder="E-Mail Address" required="">
email.send_keys("xyz@abc.com")
time.sleep(2)

message = driver.find_element(By.NAME, "message")
#<textarea name="message" rows="6" class="form-control" id="message" placeholder="Your Message" required=""></textarea>
message.send_keys("Good and useful website.")
time.sleep(2)

button = driver.find_element(By.ID, "form-submit")
#<button type="submit" id="form-submit" class="main-button">Send Message</button>
button.click()

time.sleep(10)

print("OK")
driver.quit()