from behave import *
from colorama import init

use_step_matcher('re')
init()


# region >>>STEP<<<

@step(r'I am on the "(.+)" product listing page')
def step_impl(context, product_category):
    assert context.product_page.is_title_correct(product_category), \
        "Product listing page title is incorrect."


# region >>>WHEN<<<

@when("I click on the first product's READ MORE button")
def step_impl(context):
    context.first_product_name = context.product_page.get_first_product_name()
    context.product_page.click_first_product_read_more_button()


# region >>>THEN<<<

@then(r'each product should display its name, detail and image')
def step_impl(context):
    assert context.product_page.are_elements_visible(), \
        "Product listing page elements are not visible."


@then(r'I am on the product detail page')
def step_impl(context):
    product_name = context.first_product_name
    assert context.product_details_page.is_title_correct(product_name), \
        "Product detail page title is incorrect."
    assert context.product_details_page.are_elements_visible(), \
        "Product detail page elements are not visible."
