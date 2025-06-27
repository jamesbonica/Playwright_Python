import pytest
from playwright.sync_api import sync_playwright, Page
from pages.orangehrm_home_page import HomePage
from pages.orangehrm_login_page import LoginPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

