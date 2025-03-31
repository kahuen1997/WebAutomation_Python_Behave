import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'U open the broswer')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'U open the website')
def step_impl(context):
    context.driver.get("https://mvnrepository.com/")
    context.driver.maximize_window()


@when(u'U enter the name of search "{searchbar}"')
def step_impl(context, searchbar):
    element = context.driver.find_element(by=By.XPATH,value="//input[@id='query']")
    element.send_keys(searchbar)


@then(u'U click Search Button')
def step_impl(context):
    element = context.driver.find_element(by=By.XPATH,value="//input[@value='Search']")
    element.click()

@then(u'User Verfiy page and close the browser')
def step_impl(context):
    time.sleep(5)
    context.driver.quit()

# Scenario
@when(u'U click the chart')
def step_impl(context):
    element = context.driver.find_element(by=By.XPATH,value="//div[@class='box box-stats']//div[@class='box-content']//a//*[name()='svg']//*[name()='rect'][1]")
    element.click()


@when(u'User Verfiy page and close the browser')
def step_impl(context):
    time.sleep(10)
    context.driver.quit()

