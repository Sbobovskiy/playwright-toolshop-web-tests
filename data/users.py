import time

VALID_EMAIL = "customer@practicesoftwaretesting.com"
VALID_PASSWORD = "welcome01"


def new_user():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "birth_date": "1990-01-15",
        "country": "UA",
        "postal_code": "33000",
        "house_number": "12",
        "street": "Shevchenka",
        "city": "Rivne",
        "state": "Rivnenska",
        "phone": "380991234567",
        "email": f"user{int(time.time())}@example.com",
        "password": "Str0ng!Pass123",
    }