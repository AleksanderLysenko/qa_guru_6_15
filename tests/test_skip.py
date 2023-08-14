"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have
from selene.support.shared import browser


def is_desktop(width):
    return width > 1000


def test_github_desktop(browser_param):
    if not is_desktop(browser.config.window_width):
        pytest.skip("Соотношение сторон для мобильной версии")
    browser.open('')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_param):
    if is_desktop(browser.config.window_width):
        pytest.skip("Соотношение сторон для десктопной версии")
    browser.open('')
    browser.element('.Button--link .Button-label').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
