from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser= webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.youtube.com')
i=0 
while i<5:
    #Refreshes the web page 5times with 30 seconds interval
    browser.refresh()
    print("refreshed: {}".format(i))
    time.sleep(30)
    i+=1