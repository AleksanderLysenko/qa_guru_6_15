"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import have
from selene.support.shared import browser


def test_github_desktop(browser_size_desktop):
    browser.open('')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_size_mobile):
    browser.open('')
    browser.element('.Button--link .Button-label').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
