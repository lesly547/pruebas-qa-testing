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
    def setUp(self): # Inicializamos el driver requerido en selenium para la prueba front

    def test_status(self): # Este test incluye la prueba de back donde comprobamos el código y la fuente de la respuesta.

    def test_buscador(self): # Este test incluye la prueba donde se navega a través de la web, usando las herramientas de selenium   

    def tearDown(self): # Cerramos el driver 

if __name__ == "__main__":
 unittest.main()

