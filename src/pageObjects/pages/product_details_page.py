from selenium.webdriver.common.by import By

from src.pageObjects.pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    PRODUCT_DETAILS = (By.CLASS_NAME, 'shop_product_description')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="shop_product_description"]/h1')
    PRODUCT_TEXT = (By.XPATH, '//div[@class="shop_product_description"]/p')
    PRODUCT_IMAGE = (By.XPATH, '//div[@class="inner"]//img')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def are_elements_visible(self) -> bool:
        return all([
            self.is_element_visible(self.PRODUCT_DETAILS),
            self.is_element_visible(self.PRODUCT_TITLE),
            self.is_element_visible(self.PRODUCT_TEXT),
            self.is_element_visible(self.PRODUCT_IMAGE),
        ])
