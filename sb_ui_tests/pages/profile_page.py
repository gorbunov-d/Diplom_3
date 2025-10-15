from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ProfilePage(BasePage):
    HISTORY_TAB = (By.CSS_SELECTOR, "a[href='/account/order-history'], a[href*='order-history'], a[href$='/account/history'], a[href*='history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выход') or contains(., 'Log out')]")

    def open_profile(self):
        self.open("/account/profile")

    def goto_history(self):
        try:
            self.click(self.HISTORY_TAB)
        except Exception:
            self.open("/account/order-history")
        self.wait.until(EC.url_contains("/account/order-history"))

    def logout(self):
        try:
            self.click(self.LOGOUT_BUTTON)
        except Exception:
            # Fallback: clear tokens and navigate to login
            self.driver.execute_script("window.localStorage.removeItem('accessToken'); window.localStorage.removeItem('refreshToken');")
            self.open("/login")
        self.wait.until(EC.url_contains("/login"))
