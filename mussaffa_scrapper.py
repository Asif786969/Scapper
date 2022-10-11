from selenium.webdriver.common.by import By
from selenium import webdriver
import time
path="C:\\Users\\mohasif6\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.get("https://screener.musaffa.com/cabinet/onboarding")
driver.find_element(By.CLASS_NAME, 'img-logo')
time.sleep(3)
# driver.quit()