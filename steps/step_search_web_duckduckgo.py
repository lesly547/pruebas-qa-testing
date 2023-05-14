import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")
firefoxpath = os.path.join(script_dir, "drivers/geckodriver")

driver = webdriver.Chrome(executable_path=chromepath)


@given(u"open duckduckgo web")
def open_duckduckgo_web(context):
    driver.get("https://duckduckgo.com/")
    driver.maximize_window()
    time.sleep(2)


@when(u"user searches {city} on the web")
def user_searches_on_the_web(context, city):
    driver.find_element(By.XPATH, "//input[@id='search_form_input_homepage']").send_keys(city, Keys.ENTER)
    time.sleep(2)


@then(u"enter to {city} - {value} result")
def enter_to_result(context, city, value):
    driver.find_element(By.XPATH, "//span[contains(text(),'" + city + " - " + value + ", la enciclopedia libre')]").click()
    time.sleep(2)
    driver.close()
