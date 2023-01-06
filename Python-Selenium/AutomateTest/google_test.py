from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
name = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'q')))
name.send_keys("كيف أصبح مليونير")
clickBtn =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'btnK')))
clickBtn.click()
