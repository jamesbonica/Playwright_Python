import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("banner").get_by_role("img", name="profile picture").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.locator("form")).to_contain_text("Password")
