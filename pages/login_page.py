from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random
import string


def generate_password(length=9):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.sample(characters, length))
    return password


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form should be present'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"Login" should be present in url'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form should be present'

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        email.send_keys(str(time.time()) + '@fakemail.org')
        new_password = generate_password()
        password.send_keys(new_password)
        confirm_password.send_keys(new_password)
        time.sleep(3)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()



'''#my
rom .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPageLocators(self, link)
        page.open()
        page.should_be_login_url()
    assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True'''