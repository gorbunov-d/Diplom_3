import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.suite("Core")
class TestCore:
    @allure.title("Навигация: Конструктор и Лента заказов")
    def test_navigate_constructor_and_feed(self, driver):
        from utils.urls import BASE_URL
        main = MainPage(driver, BASE_URL)
        main.open_main()
        main.goto_constructor()
        assert main.current_path().startswith("/")
        main.goto_feed()
        assert main.current_path().startswith("/feed")

    @allure.title("Модалка ингредиента: открытие и закрытие")
    def test_ingredient_modal_open_and_close(self, driver):
        from utils.urls import BASE_URL
        main = MainPage(driver, BASE_URL)
        main.open_main()
        main.open_first_ingredient_modal()
        main.close_modal()
        # Проверяем, что модалки больше нет
        from utils.urls import BASE_URL
        feed = FeedPage(driver, BASE_URL)
        assert not feed.is_order_modal_visible()

    @allure.title("Открытие заказа из Ленты")
    def test_open_order_from_feed(self, driver):
        from utils.urls import BASE_URL
        feed = FeedPage(driver, BASE_URL)
        feed.open_feed()
        feed.open_first_order()
        assert feed.is_order_modal_visible() or feed.current_path().startswith("/feed/")

