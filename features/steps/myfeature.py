from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Launch the browser')
def step_launch(context):
    context.driver = webdriver.Chrome()

@when(u'Open WebDriver Page')
def step_OpenPage(context):
    context.driver.get("https://www.selenium.dev/documentation/webdriver/")

@then(u'Verify that the logo present on page')
def step_VerifyLogo(context):
    element = context.driver.find_element(by=By.XPATH,value="//h1[normalize-space()='WebDriver']")
    assert element.is_displayed()
    clickelement = context.driver.find_element(by=By.XPATH,value="//a[normalize-space()='Getting started']")
    clickelement.click()

@then(u'close Browser')
def step_Close(context):
    context.driver.quit()
