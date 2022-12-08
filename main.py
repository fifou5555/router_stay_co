from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from time import strftime
from datetime import datetime
import sys

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
    password_field.send_keys(password)
    sleep(1)
    login.click()
    sleep(3)

    # find button and click
    connect_button = connect_bot.find_element(By.CLASS_NAME, "h_connect_off")
    connect_button.click()
    sleep(20)
    connect_bot.close()


LOGIN_ADDRESS = "http://192.168.0.1/index.html#login"

print()
print()
print("Welcome to the ZTE auto-reconnect")
print()
print()
print("The default router adress is :", LOGIN_ADDRESS)
print()

router_adress_query = input("Would you like to change it ? Y or N :")
if router_adress_query.lower() == "y":
    router_address_confirmation = "n"
    while router_address_confirmation.lower() == "n":
        LOGIN_ADDRESS = input("Please write the router adress beginning with http:// : ")
        print("Router adress is :", LOGIN_ADDRESS)
        router_address_confirmation = input("Would you like to change it ? ? Y or N : ")  # <--------- CHECK HERE 

print()
print("I will need the router interface password")
print()
password = input("Please type the password :")
print()
print()
print("The default interval time for checking the conection is 5 minutes (300sec), Would you like to change it ? Y or N : ") # <--------- CONTINUE HERE 
print("Service will check if internet conection is active every 5min")
print("Starting Service....")


service1 = Service(ChromeDriverManager().install())

while True:
    try:
        # check active connection
        response = requests.head("https://www.google.com")

        # print if true
        print("\n", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": Internet connection is active")
    except requests.ConnectionError:
        # print if fail
        print("\n", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": No internet connection")
        re_connect()


    # Wait 5 minutes
    print("Next check in :")
    for remaining in range(300, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1) 