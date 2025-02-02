from selenium.webdriver.common.by import By

from src.pageObjects.pages.base_page import BasePage


class ProductPage(BasePage):
    HEADER_LOCATOR = lambda self, header_text: (By.XPATH, f'//span[text()="{header_text}"]')
    PRODUCT_LIST_COLUMN = (By.XPATH, '//div[@class="shop_productlistdynamiccolumns"]')
    PRODUCT_DETAILS = (By.XPATH, '//div[@class="details"]')
    PRODUCT_TITLE = (By.XPATH, '//strong[@class="name"]')
    PRODUCT_TEXT = (By.XPATH, '//p[@class="teaser"]')
    PRODUCT_IMAGE = (By.XPATH, '//div[@class="image"]')
    PRODUCT_READ_MORE = (By.XPATH, '//a[@class="viewproduct"]')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_first_product_read_more_button(self):
        self.click_element(*self.PRODUCT_READ_MORE)

    def are_elements_visible(self) -> bool:
        return all([
            self.is_element_visible(self.PRODUCT_LIST_COLUMN),
            self.is_element_visible(self.PRODUCT_DETAILS),
            self.is_element_visible(self.PRODUCT_TITLE),
            self.is_element_visible(self.PRODUCT_TEXT),
            self.is_element_visible(self.PRODUCT_IMAGE),
            self.is_element_visible(self.PRODUCT_READ_MORE)
        ])

    def get_first_product_name(self):
        product_name = self.driver.find_element(*self.PRODUCT_TITLE).text
        return product_name
