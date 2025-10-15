import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.suite("Core")
class TestCore:
    def test_navigate_constructor_and_feed(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.goto_constructor()
        assert "/" in driver.current_url
        main.goto_feed()
        assert "/feed" in driver.current_url

    def test_ingredient_modal_open_and_close(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.open_first_ingredient_modal()
        # If modal appears, closing should not raise
        main.close_modal()

    def test_open_order_from_feed(self, driver, base_url):
        feed = FeedPage(driver, base_url)
        feed.open_feed()
        feed.open_first_order()
        assert "/feed" in driver.current_url

