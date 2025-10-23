import allure
from .base_page import BasePage
from locators.feed_locators import COUNTER_TOTAL, COUNTER_TODAY, FIRST_ORDER, ORDER_MODAL


class FeedPage(BasePage):

    @allure.step("Open feed page")
    def open_feed(self):
        self.open("/feed")

    @allure.step("Open first order from feed")
    def open_first_order(self):
        # Дожидаемся видимости первого заказа и кликаем через базовый helper
        self.visible(FIRST_ORDER)
        self.js_click(FIRST_ORDER)
        # Единый ожидаемый результат: переход на страницу заказа
        self.wait_url_contains("/feed/")

    def is_order_modal_visible(self) -> bool:
        return self.exists(ORDER_MODAL)

    def get_counters(self) -> tuple[str, str]:
        total = self.visible(COUNTER_TOTAL).text
        today = self.visible(COUNTER_TODAY).text
        return total, today
