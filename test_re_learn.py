from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Tests.test_mainpage import Main_Page
from Tests.test_micepage import Mice_Page
from Tests.test_itempage import Item_Page


class AmazonTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=r"C:\Users\NatanFaktorovich"
                                                                                      r"\PycharmProjects"
                                                                                      r"\WebDrivers").install()))

        self.driver.get(r"https://www.amazon.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.main_page = Main_Page(self.driver)
        self.mice_page = Mice_Page(self.driver)
        self.item_page = Item_Page(self.driver)

    def test_case_1(self):
        if not self.main_page.computer_mice_exist():
            while not self.main_page.computer_mice_exist():
                self.driver.close()
                self.setUp()

        self.main_page.computer_mice_button.click()
        self.mice_page.item_num(3)
        self.item_page.show_price()

    def tearDown(self) -> None:
        self.driver.close()
