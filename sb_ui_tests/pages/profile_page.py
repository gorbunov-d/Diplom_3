import allure
from .base_page import BasePage
from locators.profile_locators import HISTORY_TAB, LOGOUT_BUTTON
from locators.login_locators import SUBMIT as LOGIN_SUBMIT
from selenium.common.exceptions import WebDriverException, TimeoutException


class ProfilePage(BasePage):

    @allure.step("Open profile page")
    def open_profile(self):
        self.open("/account/profile")
        self.accept_cookies()
        self.close_all_modals()

    @allure.step("Go to order history")
    def goto_history(self):
        # Надёжная навигация: пытаемся кликнуть по вкладке, иначе прямой переход
        try:
            self.js_click(HISTORY_TAB)
            self.wait_url_contains("/account/order-history")
        except (WebDriverException, TimeoutException):
            self.open("/account/order-history")
            self.wait_url_contains("/account/order-history")

    @allure.step("Logout")
    def logout(self):
        # Надёжная навигация: клик по кнопке выхода, иначе прямой переход
        try:
            self.js_click(LOGOUT_BUTTON)
            self.wait_url_contains("/login")
        except (WebDriverException, TimeoutException):
            self.open("/login")
            self.wait_url_contains("/login")

    def current_path(self) -> str:
        return self.driver.current_url.replace(self.base_url, "")
