from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    TOTAL_SUM = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    ADD_BOOK = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
    
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner a")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")