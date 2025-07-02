import pytest

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

