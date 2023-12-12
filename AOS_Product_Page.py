import webbrowser
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class AOS_Product_Page:
    """"This class holds HTML element and functions of the main page"""

    def __init__(self, driver: webbrowser):
        self.driver = driver

    def quantity(self, number):
        quantity = self.driver.find_element(By.CSS_SELECTOR, "[class='plus']")
        for i in range(number-1):
            quantity.click()

    def add_to_cart(self):
        add_to_cart = self.driver.find_element(By.NAME, "save_to_cart")
        add_to_cart.click()




