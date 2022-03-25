from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'----------------------------------')
    print(f'Test start at: {datetime.datetime.now()}')

    driver.maximize_window()

    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_title:
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We\'re seeing title message --{driver.title}')
        sleep(0.25)
    else:
        print(f'we\'re not at the Advantage Shopping homepage. Check your code!')


def tearDown():
     if driver is not None:
         print(f'----------------------------------')
         print(f'The test is complete at: {datetime.datetime.now()}')
         sleep(1)
         driver.close()
         driver.quit()





setUp()
tearDown()




