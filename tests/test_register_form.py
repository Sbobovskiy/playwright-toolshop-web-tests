import re
import pytest
from data.users import new_user
from playwright.sync_api import Page, expect
from pages.registration_page import RegisterPage

def test_register_form_is_displayed(page: Page):
    registration = RegisterPage(page)
    registration.open()
    expect(page).to_have_url(registration.URL)
    expect(registration.first_name).to_be_visible()
    expect(registration.email).to_be_visible()
    expect(registration.password).to_be_visible()
    expect(registration.submit).to_be_enabled()


def test_register_empty_form_shows_errors(page: Page):
    registration = RegisterPage(page)
    registration.open()
    registration.submit.click()
    expect(registration.first_name_error).to_be_visible()
    expect(registration.last_name_error).to_be_visible()
    expect(registration.email_error).to_be_visible()
    expect(registration.password_error).to_be_visible()


def test_register_success(page: Page):
    registration = RegisterPage(page)
    registration.open()
    registration.fill_form(new_user())
    registration.submit.click()
    expect(page).to_have_url(re.compile(r"/auth/login"))

