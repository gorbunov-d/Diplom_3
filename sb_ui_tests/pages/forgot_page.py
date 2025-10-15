from selenium.webdriver.common.by import By
from .base_page import BasePage


class ForgotPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "form .input input.input__textfield[type='text'], form input[name='name']")
    SUBMIT = (By.CSS_SELECTOR, "form button[type='submit'], form .button_button_type_primary__1O7Bx")

    def submit_email(self, email: str):
        self.type(self.EMAIL, email)
        self.click(self.SUBMIT)
