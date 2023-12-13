from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import ProductPageLocators
import math
import time
import random

class BasePage(): 

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (ThisSelectorNotFound):
            return False
        return True
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
 
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(2)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK_INVALID), "Login link is not presented"         
        
     
    def find_view_bsaket_button(self):
        button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        button.click()
        time.sleep(2)
    
    def basket_is_empty(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_EMPTY).text
        assert basket in "Continue shopping" , f"Such elenment not found {basket} in basket"
        
        # .text in "Your basket is empty.", "In basket is goods"
           
    def basket_is_not_empty(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_EMPTY).text
        assert basket in "basket empty" , f"Such elenment not found {basket} in basket"
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
                                                                 
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        pasword = random.randrange(111111111, 222222222)
        
        register = self.browser.find_element(*BasePageLocators.LOGIN_PAGE)
        register.click()
        time.sleep(5)
        input_email = self.browser.find_element(*BasePageLocators.EMAIL)
        input_email.send_keys(email)
        
        input_password = self.browser.find_element(*BasePageLocators.PASWORD)
        input_password.send_keys(pasword)
        
        input_confirm_password = self.browser.find_element(*BasePageLocators.CONFIRM_PASWORD)
        input_confirm_password.send_keys(pasword)
        time.sleep(3)
        
        button_register = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
        button_register.click()
        time.sleep(3)                                                             