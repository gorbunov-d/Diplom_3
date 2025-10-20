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

    @allure.step("Go to constructor")
    def goto_constructor(self):
        self.click(CONSTRUCTOR_LINK)

    @allure.step("Go to feed")
    def goto_feed(self):
        self.click(FEED_LINK)

    @allure.step("Go to login")
    def goto_login(self):
        self.click(LOGIN_LINK)

    @allure.step("Open first ingredient modal")
    def open_first_ingredient_modal(self):
        self.click(FIRST_INGREDIENT)
        self.visible(ING_MODAL)

    @allure.step("Close ingredient modal")
    def close_modal(self):
        try:
            self.click(ING_MODAL_CLOSE)
        except Exception:
            self.press_escape()

    def current_path(self) -> str:
        return self.driver.current_url.replace(self.base_url, "")
