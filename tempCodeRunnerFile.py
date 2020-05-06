from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('./assets/chromedriver')

browser.get('hhtps://www.instagram.com')

sleep(5)

browser.close()