
import csv
from getpass import getpass
from time import sleep
#from selenium.webdriver import Chrome
from msedge.selenium_tools import Edge , EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get("https://twitter.com/login")
driver.maximize_window()
sleep(5)
username = driver.find_element_by_xpath('//input[@name="text"]')
user = "@Joni50Li"
username.send_keys(user)
username.send_keys(Keys.RETURN)
sleep(5)
my_password = "contraseña123*"
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)
sleep(5)
driver.get("https://twitter.com/search?q=%23ReporteCovid19%20%23Guanajuato&src=typed_query&f=live")
sleep(10)
page_cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
sleep(5)
print(page_cards)
sleep(500000)

# close the browser window
