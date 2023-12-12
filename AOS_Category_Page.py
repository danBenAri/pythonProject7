import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Category_Page:
    """"This class holds HTML element and functions of the main page"""

    def __init__(self, driver:webbrowser):
        self.driver = driver


    def product(self):
        category_title = self.driver.find_element(By.CSS_SELECTOR, ".categoryTitle ").text
        list_id_laptops = range(1, 12)
        list_id_headphones = [12,14, 15]
        list_id_tablets = range(16, 19)
        list_id_speakers = range(19, 26)
        list_id_mices = range(26, 35)
        id_list = []

        if category_title == "LAPTOPS":
            id_list = list_id_laptops
        elif category_title == "HEADPHONES":
            id_list = list_id_headphones
        elif category_title == "TABLETS":
            id_list = list_id_tablets
        elif category_title == "SPEAKERS":
            id_list = list_id_speakers
        else:
            id_list = list_id_mices

        random_id = random.choice(id_list)
        return self.driver.find_element(By.ID, f"{random_id}")


    def product_click(self):
        self.product().click()