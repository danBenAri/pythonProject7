import random
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Home_Page:
    """"This class holds HTML element and functions of the main page"""

    def __init__(self, driver:webbrowser):
        self.driver = driver

    def category(self):
        list_id = ["speakersImg", "tabletsImg", "laptopsImg", "MiceCategory", "headphonesImg"]
        random_id = random.choice(list_id)
        return self.driver.find_element(By.ID, f"{random_id}")

    def click_category(self):
        self.category().click()



