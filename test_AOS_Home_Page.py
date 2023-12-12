from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint, choice

from AOS_Category_Page import AOS_Category_Page
from AOS_Home_Page import AOS_Home_Page
from AOS_Product_Page import AOS_Product_Page


class TestAOS_Home_page(TestCase):

    def setUp(self):
        # Create an object of type Service that contains the location of the chromedriver
        service_chrome = Service(r"C:\Users\danie\Selenium\chromedriver-win64\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to AOS URL
        self.driver.get("https://www.advantageonlineshopping.com/#/")

        self.driver.maximize_window()

        # When an element is not found, there will be a timeout of 10 seconds
        self.driver.implicitly_wait(10)

        # Create an object
        self.home_page = AOS_Home_Page(self.driver)
        self.category_page = AOS_Category_Page(self.driver)
        self.product_page = AOS_Product_Page(self.driver)


    def test_for_me(self):
        self.home_page.click_category()
        self.category_page.product_click()
        self.product_page.quantity(4)
        self.product_page.add_to_cart()
        

    def test_question1(self):
        pass


    def tearDown(self):
        sleep(5)
