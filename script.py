from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from random import randint
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
# Time to wait for element's presence
driver.implicitly_wait(10)
driver.get('https://www.instagram.com/')

# Sleep a random number of seconds (between 5 and 10)
sleep(randint(5,10))

# # Click 'Accept cookies' button on www.instagram.com
# accept_cookis_button = driver.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]')
# accept_cookis_button.click()

# sleep(randint(5,10))

username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
username_input.send_keys("yourUsername")
password_input.send_keys("yourP@ssw0rd")

sleep(randint(5,10))

login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

# Close the browser after 100 seconds
sleep(5)
driver.close()