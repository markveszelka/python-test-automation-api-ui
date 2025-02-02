from behave import *
from colorama import init

use_step_matcher('re')
init()


# region >>>GIVEN<<<

@step(r'I navigate to the "(.+)" category within Products')
def step_impl(context, product_category):
    context.base_page.hover_over_element(context.home_page.PRODUCTS_MENU_LOCATOR)
    category_element = context.driver.find_element(*context.home_page.PRODUCT_DROPDOWN_SUBMENU_LOCATOR(product_category))
    category_element.click()
