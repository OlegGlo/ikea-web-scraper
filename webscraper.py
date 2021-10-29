#sheeesh

import requests
from selenium import webdriver

import time
import sys
from selenium.webdriver.chromium.webdriver import ChromiumDriver

from selenium.webdriver.firefox.options import Log

'''
URL = "https://www.ikea.com/ca/en/shoppingcart/"
page = requests.get(URL)
print(page.text)
'''

# If logged in -> shopping cart -> check out since everything is there already
# Else log in and -> shopping cart

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

LOG = "olegglotov99@gmail.com"
PAS = "Aimkoler12"

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:

    #website open
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.ikea.com/ca/en/profile/login")

    #login to account
    login_text_field = driver.find_element(By.ID, "username")
    password_text_field = driver.find_element(By.ID, "password")
    login_text_field.send_keys(LOG)
    password_text_field.send_keys(PAS)
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/form/button[1]")
    login_button.click()

    #navigate to shopping cart
    time.sleep(3)
    driver.get("https://www.ikea.com/ca/en/shoppingcart/")

    #click checkout
    time.sleep(3)
    checkout_button = driver.find_element(By.XPATH, "/html/body/main/main/div/div/div/div[11]/div/div[2]/div/button[2]")
    checkout_button.click()

    time.sleep(12)

    in_stock_status = True

    try:
        message = driver.find_element(By.XPATH,("//*[text()='No available shipping options']"))
        in_stock_status = False
        driver.close()
    except:
        print("no prompt")

    #check availability
    try:
        message = driver.find_element(By.XPATH,("//*[text()='We’re not able to send you the items via home delivery at the moment. Please try again tomorrow or proceed with Click and Collect. We apologize for any inconvenience.']"))
        in_stock_status = False
        driver.close()
    except:
        print("error in method")

if in_stock_status == True:
    print("item in stock")
else:
    print("item out of stock")