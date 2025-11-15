from playwright.sync_api import Page,expect
from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

        self.email = page.get_by_test_id('registration-form-email-input').locator('Input')
        self.username = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill_registration(self,
        email = "user.name@gmail.com",
        username = "username",
        password = "password"
        ):
        self.email.fill(email)
        expect(self.email).to_have_value(email)

        self.username.fill(username)
        expect(self.username).to_have_value(username)

        self.password.fill(password)
        expect(self.password).to_have_value(password)
