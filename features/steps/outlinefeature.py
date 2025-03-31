import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given(u'User Launch the Browser')
def test_Launch(context):
    context.driver = webdriver.Chrome()

@when(u'User Go to Facebook Page')
def test_Navigation(context):
    context.driver.get("https://www.facebook.com/r.php?locale=zh_TW&display=page")

@when(u'User Fill in the name"{Name}"')
def test_FillName(context, Name):
    element = context.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    assert element.is_displayed()
    element.click()
    element.send_keys(Name)

@when(u'User fill in birth"{Birth}"')
def test_Birth(context, Birth):
    element = context.driver.find_element(by=By.XPATH, value="//select[@id='year']")
    select = Select(element)
    select.select_by_visible_text(Birth)

@then(u'User Click Submit')
def test_Click(context):
    time.sleep(5)

# @then(u'User quit the browser')
# def test_Quit(context):
#     context.driver.quit()

