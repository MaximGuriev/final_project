import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('link', ["0","1","2", "3", "4", "5", "6","7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    time.sleep(3)
    
    
    
    
    