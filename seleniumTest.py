from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def login(email, password):
    # driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)
    # driver.get("https://fim.temple.edu/idp/profile/SAML2/Redirect/SSO;jsessionid=431C31C7AC88ED07B99B79EACD49E3EA?execution=e1s1")
    # driver.find_element(By.ID, "username").send_keys(email)
    # # username.clear()
    # # username.send_keys(email)

    # driver.find_element(By.ID, "password").send_keys(password)
    # # password.clear()
    # # password.send_keys(password)

    # driver.find_element(By.NAME, "_eventId_proceed").click()
    # print("Succesful Login")
    driver.get("https://fim.temple.edu/idp/profile/SAML2/Redirect/SSO;jsessionid=96B545BAC08B041245559980F67221CF?execution=e1s1")

    driver.find_element_by_xpath("//input[@id='username']").send_keys("")

    driver.find_element_by_xpath("//input[@id='password']").send_keys("")

    driver.find_element_by_xpath("//button[@class='btn btn-default btn-login']").click()
    # driver.find_element(By.ID, "username").send_keys(email)
    # driver.find_element(By.ID, "password").send_keys(password)
    # driver.find_element(By.CLASS_NAME, "btn btn-default btn-login").click()




# driver = webdriver.Chrome(executable_path="./chromedriver")
# webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.find_element_by_xpath("//input[@id='username']").send_keys("")
# driver.find_element_by_xpath("//input[@id='password']").send_keys("")
