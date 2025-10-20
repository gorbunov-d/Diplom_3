import allure
from .base_page import BasePage
from locators.profile_locators import HISTORY_TAB, LOGOUT_BUTTON


class ProfilePage(BasePage):

    @allure.step("Open profile page")
    def open_profile(self):
        self.open("/account/profile")

    @allure.step("Go to order history")
    def goto_history(self):
        try:
            self.click(HISTORY_TAB)
        except Exception:
            self.open("/account/order-history")
        # URL wait via base
        self.wait.until(lambda d: "/account/order-history" in d.current_url)

    @allure.step("Logout")
    def logout(self):
        try:
            self.click(LOGOUT_BUTTON)
        except Exception:
            # Fallback: clear tokens and navigate to login
            self.driver.execute_script("window.localStorage.removeItem('accessToken'); window.localStorage.removeItem('refreshToken');")
            self.open("/login")
        self.wait.until(lambda d: "/login" in d.current_url)

    def current_path(self) -> str:
        return self.driver.current_url.replace(self.base_url, "")
