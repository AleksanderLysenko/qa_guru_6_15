import pytest
from selene.support.shared import browser

browser.config.base_url = 'https://github.com/'


@pytest.fixture(scope="function", autouse=False)
def browser_size_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture(scope="function", autouse=False)
def browser_size_mobile():
    browser.config.window_width = 960
    browser.config.window_height = 540

    yield

    browser.quit()


@pytest.fixture(scope="function", autouse=False, params=[(1928, 1080), (960, 540)], ids=["desktop", "mobile"])
def browser_param(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()
