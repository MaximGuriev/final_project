from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium import webdriver
import pytest


class BasketPage(BasePage):
    def basket_is_empty(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_EMPTY).text
        assert basket in "Continue shopping" , f"Such elenment not found {basket} in basket"
        
        # .text in "Your basket is empty.", "In basket is goods"
           
    def basket_is_not_empty(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_EMPTY).text
        assert basket in "basket empty" , f"Such elenment not found {basket} in basket"