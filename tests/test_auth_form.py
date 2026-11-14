import re
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from data.users import VALID_EMAIL, VALID_PASSWORD


def test_login_form_is_displayed(page: Page):
    login = LoginPage(page)
    login.open()
    expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")
    expect(login.email).to_be_visible()
    expect(login.password).to_be_visible()
    expect(login.submit).to_be_enabled()


def test_login_success(page: Page):
    login = LoginPage(page)
    login.open()
    login.login(VALID_EMAIL, VALID_PASSWORD)
    expect(page).to_have_url(re.compile(r"/account"))


def test_login_wrong_password(page: Page):
    login = LoginPage(page)
    login.open()
    login.login(VALID_EMAIL, "wrong_password")
    expect(login.error).to_be_visible()


@pytest.mark.parametrize("email, password", [
    ("", ""),
    (VALID_EMAIL, ""),
    ("", VALID_PASSWORD),
])
def test_login_empty_fields(page: Page, email, password):
    login = LoginPage(page)
    login.open()
    login.login(email, password)
    expect(page).to_have_url(re.compile(r"/auth/login"))