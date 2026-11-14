from playwright.sync_api import Page


class LoginPage:
    URL = "https://practicesoftwaretesting.com/auth/login"

    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("login-submit")
        self.error = page.get_by_test_id("login-error")

    def open(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()