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
        sleep(0.75)
    else:
        print(f'we\'re not at the Advantage Shopping homepage. Check your code!')


def tearDown():
     if driver is not None:
         print(f'----------------------------------')
         print(f'The test is complete at: {datetime.datetime.now()}')
         sleep(0.75)
         driver.close()
         driver.quit()


def sign_up():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(3)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        #driver.find_element(By.XPATH, '//input[contains(@name, "usernameRegisterPage")]').send_keys(locators.username)
        sleep(0.5)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.5)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
        sleep(0.5)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
        sleep(0.5)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.firstname)
        sleep(0.5)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.lastname)
        sleep(0.5)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenumber)
        sleep(0.5)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
        sleep(0.5)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.5)
        driver.find_element(By.NAME,'addressRegisterPage').send_keys(locators.address)
        sleep(0.5)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state)
        sleep(0.5)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(0.5)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.5)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.5)
        print(f' user is signed up -************************************')


def check_full_name():
    if driver.current_url == locators.adshopcart_url:
        assert driver.find_element(By.ID,'menuUserLink').is_displayed()
        sleep(1.25)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, f'//label[contains(., " {locators.fullname}")]').is_displayed()
        print(f'The fullname {locators.fullname} is displayed: {locators.fullname}')
        sleep(0.5)


def check_orders():
      print(f'****************-No orders-*****************************')
      assert driver.find_element(By.ID, 'menuUser').is_displayed()
      sleep(1.25)
      driver.find_element(By.ID, 'menuUser').click()
      sleep(0.5)
      driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
      sleep(2)
      #driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., " No orders ")]').is_displayed()
      #sleep(1.5)
      print(f'************* No orders found.*******************************')




def log_out():
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(1.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    sleep(0.5)
    print(f'***********- Sign 0ut from account-****************************')



def log_in():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(1.25)
        driver.find_element(By.NAME,'username').send_keys(locators.new_username)
        sleep(0.5)
        driver.find_element(By.NAME,'password').send_keys(locators.new_password)
        sleep(0.5)
        driver.find_element(By.ID,'sign_in_btnundefined').click()
        sleep(0.5)
        print(f'**************-New user signed in-*************************')



def delete_test_account():
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(1.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(1.5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #driver.find_element(By.CLASS_NAME,'deleteBtnText').click()
    #driver.find_element(By.XPATH, '//button[contains(.,"Delete Account" ').click()
    driver.find_element(By.CSS_SELECTOR,'div.deleteBtnText').click()
    sleep(1.5)
    driver.find_element(By.CLASS_NAME, 'deletePopupBtn.deleteRed').click()
    sleep(3)
    print(f'************Account is deleted*******************')

    # try to login with non-exiting credential

    #assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    #sleep(2)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.NAME,'username').send_keys(locators.new_username)
    sleep(0.5)
    driver.find_element(By.NAME,'password').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    driver.find_element(By.ID,'signInResultMessage').is_displayed()
    sleep(0.5)
    driver.find_element(By.XPATH,'//label[contains(., "Incorrect user name or password")]').click()
    sleep(0.5)
    print(f'incorrect username and password is displayed!')
    print(f'-************-Test passed and account successfully deleted-*************')
    sleep(0.5)



def check_homepage():
    driver.get(locators.adshopcart_url)
    sleep(1)
    for i in locators.list_item:
       if driver.find_element(By.XPATH, f"//span[contains(., '{i}')]").is_displayed():
           print(f'{i} Item is displayed on the homepage!')
       else:
           print(f'{i} Item is not displayed!')

       # for i in range(len(locators.list_item)):
    #    # assert driver.find_element(By.XPATH, f'//span[contains(., "{locators.list_item[i]}")]').send_keys(locators.list_item)
    #    assert driver.find_element(By.XPATH, f'//span[contains(., "{locators.list_item[i]}")]').is_displayed()
    #    sleep(1)
    #    checklist_item = driver.find_element(By.XPATH, f'//span[contains(., "{locators.list_item[i]}")]').is_displayed()
    #  print(f'-- The {locators.list_item[i]} text is displayed: {checklist_item}'
    driver.find_element(By.XPATH, '//a[normalize-space()="OUR PRODUCTS"]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH,'//a[normalize-space()="OUR PRODUCTS"]').is_displayed():
        sleep(0.5)
        print(f'*****************OUR PRODUCTS ARE DISPLAYED*************************')
    else:
        print(f'***************OUR PRODUCTS ARE NOT DISPLAYED*************************')


    driver.find_element(By.XPATH, '//a[normalize-space()="SPECIAL OFFER"]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH,'//h3[contains(.,"SPECIAL OFFER")]').is_displayed():
        sleep(0.5)
        print(f'**********SPECIAL OFFER IS VISIBLE*************')
    else:
        print(f'SPECIAL OFFER IS NOT AVAILABLE')


    driver.find_element(By.XPATH, '//a[normalize-space()="POPULAR ITEMS"]').click()
    sleep(0.75)
    if driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed():
        sleep(0.5)
        print(f'************POPULAR ITEMS ARE VISIBLE**********************')
    else:
        print(f'*************POPULAR ITEMS ARE NOT VISIBLE*******************')


    driver.find_element(By.XPATH, '//a[normalize-space()="CONTACT US"]').click()
    sleep(0.75)
    if driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed():
        sleep(0.5)
        print(f'****************CONTACT US IS VISIBLE*******************')
    else:
        print(f'**************** CONTACT US IS NOT VISIBLE******************************')


       # driver.find_element(By.CSS_SELECTOR, 'li:nth-child(5) a:nth-child(1)').click()
       # sleep(0.75)
   # assert driver.find_element(By.XPATH, '//span[normalize-space()="dvantage"]/..//span[@class="logoDemo roboto-light ng-binding"]').is_displayed()
   # checkadvantage_logodemo = driver.find_element(By.XPATH, '//span[normalize-space()="dvantage"]/..//span[@class="logoDemo roboto-light ng-binding"]').is_displayed()
   #  sleep(1)
   #  print(f'****** Advantage and LogoDemo is displayed:{checkadvantage_logodemo}')


    if driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').is_displayed() and driver.find_element(By.XPATH, '//span[contains(., "DEMO")]').is_displayed():
        sleep(0.5)
        print(f'****The logo is displayed: dvantage DEMO.****')
    else:
        print('The logo is not displayed, check your code.')



    #driver.find_element(By.XPATH,'//h1[@class="roboto-bold contact_us ng-scope"]').is_displayed()
    driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    sleep(0.5)
    Select(driver.find_element(By.XPATH,'//select[@name="categoryListboxContactUs"]')).select_by_visible_text('Laptops')
    sleep(0.5)
    Select(driver.find_element(By.XPATH, '//select[@name="productListboxContactUs"]')).select_by_visible_text('HP Chromebook 14 G1(ES)')
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[contains(@name, "emailContactUs")]').send_keys(locators.email)
    # driver.find_element(By.XPATH, '//input[contains(@name, "usernameRegisterPage")]').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(2)
    # driver.find_element(By.XPATH, '//button[@id="send_btnundefined"]').click()
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)

    if driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]').is_displayed():
        sleep(0.5)
        print(f' Continue Shopping button is displayed!')
    else:
        print(f'Continue Shopping button is not displayed!')











# setUp()
# sign_up()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# check_homepage()
# tearDown()




