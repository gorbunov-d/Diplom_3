import allure
from utils.urls import BASE_URL
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


@allure.suite("Profile")
class TestProfile:
    @allure.title("Переход в личный кабинет из шапки")
    def test_open_profile_from_header(self, driver):
        main = MainPage(driver, BASE_URL)
        main.open_main()
        main.goto_login()
        assert "/login" in main.current_path()

    @allure.title("История заказов и выход из аккаунта")
    def test_history_section_and_logout(self, driver, authorized_session):
        main = MainPage(driver, BASE_URL)
        main.open_main()
        # логинимся через UI, пользователь создан через API фикстурой authorized_session
        main.goto_login()
        lp = LoginPage(driver, BASE_URL)
        creds = authorized_session["creds"]
        lp.login(creds["email"], creds["password"])
        profile = ProfilePage(driver, BASE_URL)
        profile.open_profile()
        profile.goto_history()
        assert "/account/order-history" in profile.current_path()
        profile.logout()
        assert "/login" in profile.current_path()
