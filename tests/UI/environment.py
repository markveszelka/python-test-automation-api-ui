from behave import *
from src.lib.drivers.chrome_driver_provider import ChromeDriver
from src.lib.helpers.allure_screen_shot_helper import ScreenshotHelper
from src.pageObjects.pages.base_page import BasePage
from src.pageObjects.pages.home_page import HomePage
from src.pageObjects.pages.product_details_page import ProductDetailsPage
from src.pageObjects.pages.product_page import ProductPage


@fixture
def browser_chrome(context):
    """
    Fixture method to initialize the Chrome browser.
        If you want to run tests locally, you CAN set headless=True or False.
        If you want to run tests in Docker container, you MUST set headless=True.
    """
    context.driver = ChromeDriver(headless=True).get_driver()
    yield context.driver
    context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)

    context.base_page = BasePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.product_page = ProductPage(context.driver)
    context.product_details_page = ProductDetailsPage(context.driver)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        ScreenshotHelper.take_screenshot(context.driver, scenario.name)

    if context.driver:
        context.driver.quit()
