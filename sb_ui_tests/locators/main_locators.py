from selenium.webdriver.common.by import By


CONSTRUCTOR_LINK = (By.CSS_SELECTOR, 'a[href="/"]')
FEED_LINK = (By.CSS_SELECTOR, 'a[href="/feed"]')
LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/account"], a[href^="/login"]')

FIRST_INGREDIENT = (By.CSS_SELECTOR, 'ul.BurgerIngredients_ingredients__list__2A-mT a.BurgerIngredient_ingredient__1TVf6')
ING_MODAL = (By.CSS_SELECTOR, ".Modal_modal__P3_V5 .Modal_modal__container__Wo2l_")
ING_MODAL_CLOSE = (By.CSS_SELECTOR, '.Modal_modal__P3_V5 .Modal_modal__close__TnseK, .Modal_modal__P3_V5 button')


