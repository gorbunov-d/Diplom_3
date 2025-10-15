from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, 'a[href="/"]')
    FEED_LINK = (By.CSS_SELECTOR, 'a[href="/feed"]')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/account"], a[href^="/login"]')

    FIRST_INGREDIENT = (By.CSS_SELECTOR, 'ul.BurgerIngredients_ingredients__list__2A-mT a.BurgerIngredient_ingredient__1TVf6')
    ING_MODAL = (By.CSS_SELECTOR, ".Modal_modal__P3_V5 .Modal_modal__container__Wo2l_")
    ING_MODAL_CLOSE = (By.CSS_SELECTOR, '.Modal_modal__P3_V5 .Modal_modal__close__TnseK, .Modal_modal__P3_V5 button')

    def open_main(self):
        self.open("/")

    def goto_constructor(self):
        self.click(self.CONSTRUCTOR_LINK)

    def goto_feed(self):
        self.click(self.FEED_LINK)

    def goto_login(self):
        self.click(self.LOGIN_LINK)

    def open_first_ingredient_modal(self):
        self.click(self.FIRST_INGREDIENT)
        self.visible(self.ING_MODAL)

    def close_modal(self):
        try:
            self.click(self.ING_MODAL_CLOSE)
        except Exception:
            self.press_escape()
