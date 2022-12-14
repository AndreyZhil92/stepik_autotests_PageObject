import time

import pytest

from .pages.product_page import BookOrderPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    title = page.get_product_title()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_at_messages(title)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookOrderPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookOrderPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_at_messages()


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_messages()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_msg()


@pytest.mark.parametrize('link', links)
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser, link):
        page = BookOrderPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = f"{str(time.time())}@fakemail.org"
        login_page.register_new_user(email=email, password="Siber!550")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = BookOrderPage(browser, link)
        page.open()
        page.should_not_be_at_messages()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = BookOrderPage(browser, link)
        page.open()
        title = page.get_product_title()
        page.should_be_add_to_basket_btn()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_at_messages(title)