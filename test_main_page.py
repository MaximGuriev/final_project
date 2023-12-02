import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(5)
