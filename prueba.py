# Prueba de automatización Selenium con Python
# --------------------------------------------
import os
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")
firefoxpath= os.path.join(script_dir, "drivers/geckodriver")
class PythonSelenium(unittest.TestCase) :
    def setUp(self):

    def test_status(self):

    def test_buscador(self):    

    def tearDown(self):

if __name__ == "__main__":
 unittest.main()

