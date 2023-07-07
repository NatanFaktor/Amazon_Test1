from selenium import webdriver
from selenium.webdriver.common.by import By

class Item_Page:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def show_price(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "[id='corePrice_feature_div']>div>span>span")
        print(items[1].text)
