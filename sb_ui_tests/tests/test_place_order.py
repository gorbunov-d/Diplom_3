import allure
from pages.main_page import MainPage


@allure.suite("Order")
class TestPlaceOrder:
    def test_logged_in_user_can_place_order(self, driver, base_url, authorized_session):
        main = MainPage(driver, base_url)
        main.open_main()
        assert "login" not in driver.current_url
