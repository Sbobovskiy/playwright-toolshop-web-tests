# playwright-toolshop-web-tests

UI tests for the demo web shop https://practicesoftwaretesting.com
Stack: Python, pytest, Playwright, Page Object pattern.

## What is covered
- Login form: form is displayed, successful login, wrong password, empty fields (parametrized)

## Setup
pip install -r requirements.txt
playwright install chromium

## Run
pytest --headed

## Project structure
- pages/  - Page Objects
- tests/  - test cases and fixtures
- data/   - test data
