import pytest
from selene import browser


@pytest.fixture(params=[(1280, 920), (1024,721)], ids=['desktop', 'mobile'])
def configure_general_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    is_mobile = True if width <= 1024 else False

    return is_mobile


@pytest.fixture(params=[(1280, 920)], ids=['desktop'])
def configure_desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1024,721)], ids=['mobile'])
def configure_mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
