import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
 
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get('https://medium.com/')
# time.sleep(5)
link = driver.find_element_by_link_text('See all topics')
# time.sleep(5)
link.click()
driver.get('https://medium.com/topic/art')
# try:
#     element = WebDriverWait(driver,10).until(
#         expected_conditions.presence_of_all_elements_located(By.LINK_TEXT,"u-flex0 u-height180 u-backgroundCover")
#     )
# except:
#     print("exception occred")
#     driver.quit()

time.sleep(5)
# driver.quit()