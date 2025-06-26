from typing import Any
import pytest
import re
from playwright.async_api import expect

'''
@pytest.mark.asyncio(loop_scope="module")
async def test_open_google(page: Any):
    await page.goto("https://www.google.com")
    assert "Google" in await page.title()

'''
@pytest.mark.asyncio(loop_scope="module")
async def test_google_search(page: Any):
    await page.wait_for_timeout(3000)
    await page.goto('https://google.com/ncr')

    try:
        await page.get_by_role('button', name='Accept all').click(timeout=3000)
    except:
        print('No popup')

    await page.get_by_role('combobox', name='Search').fill('Playwright Python')
    await page.keyboard.press('Enter')

    await expect(page).to_have_title(re.compile('Playwright', re.IGNORECASE))
