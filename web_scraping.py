
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
sleep(3)
driver.get("https://twitter.com/search?q=%23ReporteCovid19%20%23Guanajuato&src=typed_query&f=live")
driver.maximize_window()
sleep(5)


def get_tweet_data (filtered_element):
    
    try:
        date = filtered_element.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    except NoSuchElementException:
        return
    sleep(3)
    try:
        images =  filtered_element.find_element_by_xpath('.//div[@data-testid="tweetPhoto"]/div[1]').click()
        sleep(1)
        My_pic = pyautogui.screenshot()
        My_pic.save(r'Imagen_detection\imagenes'+"/"+date+".png")
    except NoSuchElementException:
        return
    try:
        driver.find_element_by_xpath("//div[@aria-label='Cerrar']").click()
    except NoSuchElementException:
        return
    return date

dates = []
scrolling = True
last_pos = driver.execute_script("return window.pageYOffset;")

while scrolling:
    filtered_elements = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
    for filtered_element in filtered_elements[-2:]:
        image_info = get_tweet_data(filtered_element)
        dates.append(image_info)

    scroll_atemp = 0
    while True :
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(3)
        current_pos = driver.execute_script("return window.pageYOffset;")
        if last_pos == current_pos:
            scroll_atemp +=1
            if scroll_atemp >=3:
                scrolling = False
                break
            else: sleep(3)
        else:
            last_pos = current_pos
            break
        

