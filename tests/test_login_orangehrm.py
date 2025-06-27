import time
from turtle import isvisible
from playwright.sync_api import Page, expect
from pages.orangehrm_home_page import HomePage
from pages.orangehrm_login_page import LoginPage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.login('Admin', 'admin123')
    
    expect(home_page.upgrade_button).to_be_visible()

    home_page.click_performance()
    home_page.click_dashboard()


