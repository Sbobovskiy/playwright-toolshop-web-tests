from playwright.sync_api import Page


class RegisterPage:
    URL = "https://practicesoftwaretesting.com/auth/register"

    def __init__(self, page: Page):
        self.page = page
        #fields
        self.first_name = page.get_by_test_id("first-name")
        self.last_name = page.get_by_test_id("last-name")
        self.birth_date = page.get_by_test_id("dob")
        self.country = page.get_by_test_id("country")
        self.postal_code = page.get_by_test_id("postal_code")
        self.house_number = page.get_by_test_id("house_number")
        self.street = page.get_by_test_id("street")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.phone = page.get_by_test_id("phone")
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("register-submit")
        #errors
        self.first_name_error = page.get_by_test_id("first-name-error")
        self.last_name_error = page.get_by_test_id("last-name-error")
        self.dob_error = page.get_by_test_id("dob-error")
        self.country_error = page.get_by_test_id("country-error")
        self.postal_code_error = page.get_by_test_id("postal_code-error")
        self.house_number_error = page.get_by_test_id("house_number-error")
        self.street_error = page.get_by_test_id("street-error")
        self.city_error = page.get_by_test_id("city-error")
        self.state_error = page.get_by_test_id("state-error")
        self.phone_error = page.get_by_test_id("phone-error")
        self.email_error = page.get_by_test_id("email-error")
        self.password_error = page.get_by_test_id("password-error")

    def open(self):
        self.page.goto(self.URL)

    def fill_form(self, data: dict):
        self.first_name.fill(data["first_name"])
        self.last_name.fill(data["last_name"])
        self.birth_date.fill(data["birth_date"])
        self.country.select_option(data["country"])
        self.postal_code.fill(data["postal_code"])
        self.house_number.fill(data["house_number"])
        self.street.fill(data["street"])
        self.city.fill(data["city"])
        self.state.fill(data["state"])
        self.phone.fill(data["phone"])
        self.email.fill(data["email"])
        self.password.fill(data["password"])