import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def login():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://facebook.com")
    log=driver.find_element_by_id("email")
    pas=driver.find_element_by_id("pass")
    log.send_keys("your mail here")
    pas.send_keys("your pass here")
    driver.find_element_by_name("login").click()
    sleep(20)
    driver.close()

login()