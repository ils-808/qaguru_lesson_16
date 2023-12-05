"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from model.application_manager import app


@pytest.mark.parametrize('configure_general_browser', [(1280, 920)], indirect=True)
def test_github_desktop(configure_general_browser):
    app.main_desktop.open()
    app.main_desktop.click_signin()
    app.main_desktop.should_have_title_signin()


@pytest.mark.parametrize('configure_general_browser', [(1024, 720)], indirect=True)
def test_github_mobile(configure_general_browser):
    app.main_mobile.open()
    app.main_mobile.click_signin()
    app.main_mobile.should_have_title_signin()
