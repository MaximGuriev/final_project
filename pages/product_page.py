from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium import webdriver
import pytest

class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()
        self.solve_quiz_and_get_code()
        t_sum = self.browser.find_element(*ProductPageLocators.TOTAL_SUM).text
        b_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        
        b_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        b_add = self.browser.find_element(*ProductPageLocators.ADD_BOOK).text
        assert str(b_price) in str(t_sum), f'Сумма {b_price} не добавлена в корзину {t_sum}' 
        assert str(b_name) == str(b_add), f'Должно быть название "{b_name}" а добавляется "{b_add}"' 
        
     
    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Login link is not presented"
        
           
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Messages is disappeared after adding product to basket"
   
   