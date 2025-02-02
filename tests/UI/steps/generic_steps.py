from behave import *
from colorama import init

use_step_matcher('re')
init()


# region >>>GIVEN<<<

@given(r'I am on the "(.+)" page')
def step_impl(context, page):
    context.base_page.load_given_page(page)
