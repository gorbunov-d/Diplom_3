import allure
from utils.urls import BASE_URL
from pages.main_page import MainPage


@allure.suite("Order")
class TestPlaceOrder:
    @allure.title("Залогиненный пользователь может оформить заказ (предусловие: авторизация)")
    def test_logged_in_user_can_place_order(self, driver, web_authorized_session):
        main = MainPage(driver, BASE_URL)
        main.open_main()
        assert "/login" not in main.current_path()
