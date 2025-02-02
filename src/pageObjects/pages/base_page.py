import time
from selenium.webdriver import ActionChains
from src.pageObjects.constants.constants import *
from selenium.webdriver.remote.webelement import WebElement
from colorama import Fore, Style, init

init()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, value):
        self.driver.find_element(by, value).click()

    def hover_over_element(self, locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()

    def is_element_visible(self, locator) -> bool:
        try:
            element: WebElement = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            print(f'Error occurred while checking element visibility: {e}')
            return False

    def is_title_correct(self, title):
        page_title = self.driver.title
        return title in page_title

    def load_given_page(self, page):
        print("LOAD GIVEN PAGE")
        if page.lower() == 'home':
            self.driver.get(URLs.HOME_PAGE_URL)
            self.driver.add_cookie({
                'name': 'SystemCookieChoiceDecision',
                'value': '1=30'
            })
            time.sleep(1)
            self.driver.refresh()
        else:
            raise ValueError(f'{Fore.YELLOW}{Style.BRIGHT}Page "{page}" is not implemented yet{Style.RESET_ALL}')
