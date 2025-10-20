import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.suite("Profile")
class TestProfile:
    @allure.title("Переход в личный кабинет из шапки")
    def test_open_profile_from_header(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.goto_login()
        assert "/login" in main.current_path()

    @allure.title("История заказов и выход из аккаунта")
    def test_history_section_and_logout(self, driver, base_url, authorized_session):
        main = MainPage(driver, base_url)
        main.open_main()
        profile = ProfilePage(driver, base_url)
        profile.open_profile()
        profile.goto_history()
        assert "/account/order-history" in profile.current_path()
        profile.open_profile()
        profile.logout()
        assert "/login" in profile.current_path()
