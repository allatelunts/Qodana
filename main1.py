from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
options = Options()
options.add_argument('start-maximized')
options.add_argument('--window-size=500,500')
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('kim kardashian')
sleep(3)