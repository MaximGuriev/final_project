import pytest
from selenium import webdriver
from .pages.basket_pages import BasketPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from .pages.product_page import ProductPage
import time


# @pytest.mark.parametrize('link', ["0","1","2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
# def test_guest_can_add_product_to_basket(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    # page = ProductPage(browser, link)
    # page.open()
    # time.sleep(2)
    # page.add_to_basket()
    # time.sleep(2)
    
@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    page.should_message_disappeared()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(2)
    
    
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    
 
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = ProductPage(browser, link)
    page.open()
    page.find_view_bsaket_button()
    page.basket_is_empty()
    time.sleep(2)
    
 
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.find_view_bsaket_button()
    page.basket_is_empty()
    time.sleep(2)