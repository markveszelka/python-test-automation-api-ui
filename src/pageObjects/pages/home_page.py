from selenium.webdriver.common.by import By
from src.pageObjects.pages.base_page import BasePage


class HomePage(BasePage):
    PRODUCTS_MENU_LOCATOR = (By.XPATH, '//a[@name="Products"]')
    PRODUCT_DROPDOWN_SUBMENU_LOCATOR = lambda self, product_category: (By.XPATH, f'//a[@title="{product_category}"]')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
