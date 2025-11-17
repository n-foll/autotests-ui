from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

        self.email = Input(page, 'registration-form-email-input', 'Email')
        self.username = Input(page, 'registration-form-username-input', 'Username')
        self.password = Input(page, 'registration-form-password-input', 'Password')

    def fill_registration(self,
        email = "user.name@gmail.com",
        username = "username",
        password = "password"
        ):
        self.email.fill(email)
        self.email.check_have_value(email)

        self.username.fill(username)
        self.username.check_have_value(username)

        self.password.fill(password)
        self.password.check_have_value(password)
