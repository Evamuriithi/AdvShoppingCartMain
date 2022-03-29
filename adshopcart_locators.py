import datetime
from faker import Faker
fake = Faker(locale='en_CA')



app = 'adshopcart'
adshopcart_url = 'https://www.advantageonlineshopping.com/#/'
adshopcart_title = "\xa0Advantage Shopping"
adshopcart_account_title_page  ="\xa0Advantage Shopping"
adshopcart_account_page_url = 'https://www.advantageonlineshopping.com/#/myAccount'

new_username = fake.user_name()[0:15]
email = fake.email()
new_password = fake.password()
firstname = fake.first_name()
lastname = fake.last_name()
fullname = f'{firstname} {lastname}'[0:10]
pic_desc = f'Image submitted by{"user"}'
address = fake.street_address().replace("\n"," ")
city = fake.city()
state = fake.province_abbr()[0:10]
postalcode = fake.postalcode()[0:10]
phonenumber = fake.bothify(text='1-(###)-###-####')
ssn = fake.ssn()
description  = f'It is a sunny beautiful day! {datetime.datetime.now()}'
#username = f'{fake.user_name()}{fake.pyint(111,999)}{fake.century()}'
password = fake.password()
country = fake.current_country()


list_item = ('SPEAKERS', 'TABLETS', 'LAPTOPS', 'HEADPHONES', 'MICE')




