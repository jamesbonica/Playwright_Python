import pytest
from playwright.sync_api import Page
from pages.orangehrm_home_page import HomePage
from pages.orangehrm_login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--enable-trace",
        action="store_true",
        default=False,
        help="Enable Playwright tracing for tests",
    )

@pytest.fixture(autouse=True)
def trace_setup(context, request):
    # Check if tracing is enabled via CLI
    if not request.config.getoption("--enable-trace"):
        yield  # do nothing
        return

    # Start tracing if enabled
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path=f"trace_{request.node.name}.zip")

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)

