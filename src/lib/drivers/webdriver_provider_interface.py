from abc import ABC, abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverInterface(ABC):
    @abstractmethod
    def get_driver(self) -> WebDriver:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass
