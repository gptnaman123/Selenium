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
driver.execute_script("window.scrollBy(0,1000)", "")
driver.switch_to.frame(0)
'''
<iframe frameborder="0" id="frame-one1434677811" scrolling="no" src="https://fs2.formsite.com/res/showFormEmbed?EParam=m_OmK8apOTBHmkDZCZ6tSK_3bsAv-gQi&amp;
1434677811&amp;EmbedId=1434677811" title="" style="border: 0px; margin: 0px; padding: 0px; width: 100%;" height="1459"></iframe>
'''

file = driver.find_element(By.CLASS_NAME, "file_upload")
#<input type="file" name="RESULT_FileUpload-10" size="25" class="file_upload" id="RESULT_FileUpload-10" title="" max="5" multiple="">

time.sleep(2)
file.send_keys('C:\\Users\\hp\\Pictures\\Saved Pictures\\abc.jpg')


time.sleep(10)

print("OK")
driver.quit()