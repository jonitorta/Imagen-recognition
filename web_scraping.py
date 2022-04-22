
import csv
from getpass import getpass
from importlib.resources import path
import pathlib
from time import sleep
#from selenium.webdriver import Chrome
from msedge.selenium_tools import Edge , EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pyautogui

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get("https://twitter.com/login")
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
sleep(5)
filtered_elements = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
date = filtered_elements[0].find_element_by_xpath('.//div[2]/div[2]/div[2]').text
driver.fullscreen_window()
images =  filtered_elements[0].find_element_by_xpath('.//div[@data-testid="tweetPhoto"]/img[1]').click()
sleep(2)
My_foto = pyautogui.screenshot()
My_foto.save(r'Imagen_detection\imagenes\file_name.png')
driver.find_element_by_xpath("//div[@aria-label='Cerrar']").click()
sleep(10)
