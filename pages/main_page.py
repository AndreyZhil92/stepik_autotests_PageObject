from .base_page import BasePage #у кого то с точкой работает перед base_page
from selenium.webdriver.common.by import By
from .locators import MainPageLocators #у кого то с точкой работает перед loc...
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)


    """def should_be_login_link(self): #используется в тандеме с файлом локатор там редактируется переменная тут указывается просто переменная
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), Login link is not presented"""