from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.lib.drivers.webdriver_provider_interface import DriverInterface


class ChromeDriver(DriverInterface):
    def __init__(self, headless=False):
        self._driver = self._initialize_driver(headless)

    def _initialize_driver(self, headless: bool) -> WebDriver:
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = self._get_chrome_options(headless)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def _get_chrome_options(headless):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--window-size=1920,1080')
        else:
            chrome_options.add_argument('--start-maximized')

        return chrome_options

    def get_driver(self):
        return self._driver

    def quit(self):
        self._driver.quit()
