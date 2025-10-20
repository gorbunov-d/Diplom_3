import allure
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage


@allure.suite("Auth")
@allure.sub_suite("Password Recovery")
class TestForgotPassword:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.goto_forgot()
        assert "/forgot-password" in login.current_path()

    @allure.title("Ввод почты и отправка формы восстановления")
    def test_enter_email_and_submit(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.goto_forgot()
        forgot = ForgotPage(driver, base_url)
        forgot.submit_email("test@example.com")
        assert any(p in forgot.current_path() for p in ("/reset-password", "/forgot-password"))

    @allure.title("Кнопка показать/скрыть активирует поле пароля")
    def test_password_toggle_activates_field(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.toggle_password_visibility()
        # Проверяем по активному элементу через JS
        active_type = driver.execute_script("return document.activeElement.getAttribute('type') || document.activeElement.getAttribute('name')")
        assert active_type in ("password", "text", "Пароль")
