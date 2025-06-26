import pytest
import asyncio
from playwright.async_api import async_playwright, Browser, Page
import pytest_asyncio


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def page(browser):
    page = await browser.new_page()
    yield page
    await browser.close()


