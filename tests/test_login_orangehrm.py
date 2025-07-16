from playwright.sync_api import expect

from pages.orangehrm_home_page import HomePage
from pages.orangehrm_login_page import LoginPage


def test_example(login_page: LoginPage, home_page: HomePage):

    login_page.goto()

    login_page.login("Admin", "admin123")

    expect(home_page.upgrade_button).to_be_visible()

    home_page.click_performance()
    home_page.click_dashboard()
