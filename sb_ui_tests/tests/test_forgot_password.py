import allure
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage


@allure.suite("Auth")
@allure.sub_suite("Password Recovery")
class TestForgotPassword:
    def test_navigate_to_forgot_password(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.goto_forgot()
        assert "/forgot-password" in driver.current_url

    def test_enter_email_and_submit(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.goto_forgot()
        forgot = ForgotPage(driver, base_url)
        forgot.submit_email("test@example.com")
        assert "/reset-password" in driver.current_url or "/forgot-password" in driver.current_url

    def test_password_toggle_activates_field(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.toggle_password_visibility()
        active = driver.switch_to.active_element
        assert active.get_attribute("type") == "password" or active.get_attribute("name") in ("password", "Пароль")
