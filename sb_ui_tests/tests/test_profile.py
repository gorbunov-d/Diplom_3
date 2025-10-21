import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.suite("Profile")
class TestProfile:
    @allure.title("Переход в личный кабинет из шапки")
    def test_open_profile_from_header(self, driver):
        from utils.urls import BASE_URL
        main = MainPage(driver, BASE_URL)
        main.open_main()
        main.goto_login()
        assert "/login" in main.current_path()

    @allure.title("История заказов и выход из аккаунта")
    def test_history_section_and_logout(self, driver, web_authorized_session):
        from utils.urls import BASE_URL
        main = MainPage(driver, BASE_URL)
        main.open_main()
        profile = ProfilePage(driver, BASE_URL)
        profile.open_profile()
        profile.goto_history()
        assert "/account/order-history" in profile.current_path()
        profile.open_profile()
        profile.logout()
        assert "/login" in profile.current_path()
