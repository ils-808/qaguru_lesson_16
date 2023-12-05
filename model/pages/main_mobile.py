from selene import browser, have


class MainMobile:

    def open(self):
        browser.open('https://github.com/')

    def click_signin(self):
        browser.element('.js-details-target.Button--link ').click()
        browser.element('.HeaderMenu-link--sign-in').click()

    def should_have_title_signin(self):
        return browser.element('.auth-form-header.p-0').should(have.text('Sign in to GitHub'))