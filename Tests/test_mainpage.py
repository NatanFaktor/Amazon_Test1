from selenium import webdriver
from selenium.webdriver.common.by import By

class Main_Page:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def computer_mice(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Computer mice']")

    def click_computer_mice(self):
        self.computer_mice().click()

    