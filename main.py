from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from config import *

def re_connect():

    # start browser
    connect_bot = webdriver.Chrome(service=service1)
    connect_bot.get(LOGIN_ADDRESS)
    sleep(1)

    # find fields
    password_field = connect_bot.find_element(By.ID, "txtPwd")
    login = connect_bot.find_element(By.ID, "btnLogin")
    sleep(1)

    # send password
    password_field.send_keys(PASSWORD)
    sleep(1)
    login.click()
    sleep(3)

    # find button and click
    connect_button = connect_bot.find_element(By.CLASS_NAME, "h_connect_off")
    connect_button.click()
    sleep(20)
    connect_bot.close()


service1 = Service(ChromeDriverManager().install())

while True:
    try:
        # check active connection
        response = requests.head("https://www.google.com")

        # print if true
        print("Internet connection active")
    except requests.ConnectionError:
        # print if fail
        print("No internet connection")
        re_connect()

    # Wait 5 minutes
    time.sleep(300)