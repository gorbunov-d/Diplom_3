import allure
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage


@allure.suite("Auth")
@allure.sub_suite("Password Recovery")
class TestForgotPassword:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, driver):
        from utils.urls import BASE_URL
        login = LoginPage(driver, BASE_URL)
        login.open_login()
        login.goto_forgot()
        assert "/forgot-password" in login.current_path()

    @allure.title("Ввод почты и отправка формы восстановления")
    def test_enter_email_and_submit(self, driver):
        from utils.urls import BASE_URL
        login = LoginPage(driver, BASE_URL)
        login.open_login()
        login.goto_forgot()
        forgot = ForgotPage(driver, BASE_URL)
        forgot.submit_email("test@example.com")
        # Ожидаем единый результат: остаёмся на странице ввода почты (запрос кода отправлен)
        assert forgot.current_path() == "/forgot-password"

    @allure.title("Кнопка показать/скрыть активирует поле пароля")
    def test_password_toggle_activates_field(self, driver):
        from utils.urls import BASE_URL
        login = LoginPage(driver, BASE_URL)
        login.open_login()
        login.toggle_password_visibility()
        # Проверяем активность поля через BasePage helper (без прямого driver)
        active_type = login.get_active_element_attr("type") or login.get_active_element_attr("name")
        assert active_type in ("password", "text", "Пароль")
