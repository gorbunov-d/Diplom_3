import allure
from .base_page import BasePage
from locators.main_locators import (
    CONSTRUCTOR_LINK,
    FEED_LINK,
    LOGIN_LINK,
    FIRST_INGREDIENT,
    ING_MODAL,
    ING_MODAL_CLOSE,
)


class MainPage(BasePage):

    @allure.step("Open main page")
    def open_main(self):
        self.open("/")
        self.accept_cookies()
        self.close_all_modals()

    @allure.step("Go to constructor")
    def goto_constructor(self):
        self.open("/")

    @allure.step("Go to feed")
    def goto_feed(self):
        self.open("/feed")

    @allure.step("Go to login")
    def goto_login(self):
        # Для стабильности переходим напрямую на страницу логина
        self.open("/login")
        self.accept_cookies()
        self.close_all_modals()

    @allure.step("Open first ingredient modal")
    def open_first_ingredient_modal(self):
        self.click(FIRST_INGREDIENT)
        self.visible(ING_MODAL)

    @allure.step("Close ingredient modal")
    def close_modal(self):
        try:
            self.click(ING_MODAL_CLOSE)
            self.wait_invisible(ING_MODAL)
        except Exception:
            self.press_escape()
            self.wait_invisible(ING_MODAL)

    def is_ingredient_modal_visible(self) -> bool:
        return self.is_visible(ING_MODAL)
