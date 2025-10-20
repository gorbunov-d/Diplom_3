import allure
from .base_page import BasePage
from locators.login_locators import EMAIL, PASSWORD, SUBMIT, FORGOT_LINK, TOGGLE_PASSWORD


class LoginPage(BasePage):

    @allure.step("Open login page")
    def open_login(self):
        self.open("/login")

    @allure.step("Login as user")
    def login(self, email: str, password: str):
        self.type(EMAIL, email)
        self.type(PASSWORD, password)
        self.click(SUBMIT)

    @allure.step("Go to forgot password")
    def goto_forgot(self):
        self.click(FORGOT_LINK)

    @allure.step("Toggle password visibility")
    def toggle_password_visibility(self):
        self.click(TOGGLE_PASSWORD)
