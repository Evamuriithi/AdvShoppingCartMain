from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

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


def sign_up():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        #driver.find_element(By.XPATH, '//input[contains(@name, "usernameRegisterPage")]').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password1)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password2)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.firstname)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.lastname)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenumber)
        sleep(0.25)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME,'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.25)
        print(f' user is signed up -----------------------------')


def check_full_name():
    if driver.current_url == locators.adshopcart_url:
        assert driver.find_element(By.ID,'menuUserLink').is_displayed()
        sleep(1.5)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(1.5)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
        sleep(1.5)
        driver.find_element(By.XPATH, f'//label[contains(., " {locators.fullname}")]').is_displayed()
        print(f'The fullname {locators.fullname} is displayed: {locators.fullname}')
        sleep(1.5)


def check_orders():
      print(f'------------no orders---------------')
      assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
      sleep(1.5)
      driver.find_element(By.ID, 'menuUserLink').click()
      sleep(1.5)



      driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
      sleep(1.5)
      #driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., " No orders ")]').is_displayed()
      #sleep(1.5)
      print(f' no orders found.------------------------')




def log_out():
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(1.5)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    sleep(1.5)
    print(f'Sign 0ut from account--------------------')



def log_in():
    if driver.current_url == locators.adshopcart_url:
       driver.find_element(By.ID, 'menuUserLink').click()
       sleep(0.5)
       driver.find_element(By.NAME,'username').send_keys(locators.username)
       sleep(0.5)
       driver.find_element(By.NAME,'password').send_keys(locators.password1)
       sleep(0.5)
       driver.find_element(By.ID,'sign_in_btnundefined').click()
       sleep(0.5)
       print(f'New user signed in------------------------')



def delete_test_account():
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(1.5)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(0.5)
    #driver.find_element(By.XPATH, '//button[contains(.,"Delete Account" ').click()
    driver.find_element(By.CLASS_NAME,'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'div.deletePopupBtn.deleteRed').click()
    #driver.find_element(By.XPATH, f'//td[contains(., "deletePopupBtn deleteRed")]/../td/a[contains(., "deleteAccountConfirmed()")]').click()
    #driver.find_element(By.CLASS_NAME, 'deletePopupBtn deleteRed').click()
    sleep(2)
    # try to login with non-exiting credential
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(2)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.NAME,'username').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME,'password').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    if driver.find_element(By.ID,'signInResultMessage').is_displayed():
        print(f'incorrect username and password is displayed!')
        print(f'---Test passed and account successfully deleted-----')
    else:
        print(f'Something went wrong.')







# setUp()
# sign_up()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# tearDown()




