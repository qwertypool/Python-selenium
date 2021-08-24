import selenium
from selenium import webdriver
import time
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
#driver.get('https://diageo.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_view%3Ditil%26sysparm_fixed_query%3D%26sysparm_query%3Dactive%3Dtrue%5Eassignment_group%3D2f46f7680fbe764005148e9ce1050eff%5Esys_created_on%3Ejavascript:gs.dateGenerate(%272019-12-31%27,%2723:59:59%27)%5Estate!%3D6%26sysparm_clear_stack%3Dtrue')
driver.get('https://diageo.service-now.com')
time.sleep(5)
print("done")