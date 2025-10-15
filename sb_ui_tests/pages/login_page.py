from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "form .input input.input__textfield[type='text'], form input[name='name']")
    PASSWORD = (By.CSS_SELECTOR, "form .input input.input__textfield[type='password']")
    SUBMIT = (By.CSS_SELECTOR, "form button[type='submit'], form .button_button_type_primary__1O7Bx")
    FORGOT_LINK = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
    TOGGLE_PASSWORD = (By.CSS_SELECTOR, ".input__icon.input__icon-action, .input__icon-action")

    def open_login(self):
        self.open("/login")

    def login(self, email: str, password: str):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def goto_forgot(self):
        self.click(self.FORGOT_LINK)

    def toggle_password_visibility(self):
        self.click(self.TOGGLE_PASSWORD)
