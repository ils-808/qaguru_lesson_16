"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from model.application_manager import app


def test_github_desktop(configure_desktop_browser):
    app.main_desktop.open()
    app.main_desktop.click_signin()
    app.main_desktop.should_have_title_signin()


def test_github_mobile(configure_mobile_browser):
    app.main_mobile.open()
    app.main_mobile.click_signin()
    app.main_mobile.should_have_title_signin()
