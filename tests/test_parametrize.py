"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser
from selene import have


@pytest.mark.parametrize("browser_param", [(1928, 1080)], ids=["desktop"], indirect=True)
def test_github_desktop_indirect(browser_param):
    browser.open('')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_param", [(960, 540)], ids=["mobile"], indirect=True)
def test_github_mobile_indirect(browser_param):
    browser.open('')
    browser.element('.Button--link .Button-label').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
