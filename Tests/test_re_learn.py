from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Tests.test_mainpage import Main_Page
from Tests.test_micepage import Mice_Page
from Tests.test_itempage import Item_Page
from time import sleep

class Amazon_Test(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\Natan\Desktop\Selenium\Chorme_Webdriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get(r"https://www.amazon.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.main_page = Main_Page(self.driver)
        self.mice_page = Mice_Page(self.driver)
        self.item_page = Item_Page(self.driver)

    def test_case_1(self):
        self.main_page.click_computer_mice()
        self.mice_page.item_num(3)
        self.item_page.show_price()



