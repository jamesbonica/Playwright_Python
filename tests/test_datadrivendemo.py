import csv
import string
from playwright.sync_api import Page, expect
import pytest

def load_csv_data():
    data= []
    with open("./tests/test_data/data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def load_json_data() -> list:
    import json
    with open("./tests/test_data/data.json", "r") as file:
        data = json.load(file)
    return[(item['username'],item['password']) for item in data]

    

@pytest.mark.parametrize("username,password", load_json_data())
def test_example(page: Page, username: string, password: string) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
