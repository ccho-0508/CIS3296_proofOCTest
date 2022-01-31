from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import os

def login(user, passW, cwd):
    ser = Service("/Users/ccho/Developer/CIS3296_ProjectPro/chromedriver")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

    driver.get("https://tuportal5.temple.edu/web/home-community/student-tools")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(user)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passW)

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-login']").click()

    driver.get("https://libproxy.temple.edu/login")
    driver.get("https://librarysearch.temple.edu/users/account")


user = input("Enter TU user : ")
passW = input("Enter your password : ")
cwd = os.getcwd()
cwd +='/chromedriver'

try:
    login(user, passW, cwd)
except:
    print("Invalid Credentials.")

