import time
from selenium import webdriver
def test_openMyWeb():
    driver = webdriver.Chrome()
    driver.get("https://monmon1997.github.io/Bootstrap_Templete_All/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


