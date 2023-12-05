from selene import browser, have


class MainDesktop:

    def open(self):
        browser.open('https://github.com/')

    def click_signin(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def should_have_title_signin(self):
        return browser.element('.auth-form-header.p-0').should(have.text('Sign in to GitHub'))