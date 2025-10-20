import allure
from .base_page import BasePage
from locators.login_locators import EMAIL, SUBMIT


class ForgotPage(BasePage):

    @allure.step("Submit email for password recovery")
    def submit_email(self, email: str):
        self.type(EMAIL, email)
        self.click(SUBMIT)
