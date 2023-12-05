"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

from model.application_manager import app


def test_github_desktop(configure_general_browser):
    if configure_general_browser:
        pytest.skip('Запущен тест для мобильной версии браузера')
    app.main_desktop.open()
    app.main_desktop.click_signin()
    app.main_desktop.should_have_title_signin()


def test_github_mobile(configure_general_browser):
    if not configure_general_browser:
        pytest.skip('Запущен тест для десктопной версии браузера')
    app.main_mobile.open()
    app.main_mobile.click_signin()
    app.main_mobile.should_have_title_signin()
