from selenium.webdriver.common.by import By


HISTORY_TAB = (By.CSS_SELECTOR, "a[href='/account/order-history'], a[href*='order-history'], a[href$='/account/history'], a[href*='history']")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выход') or contains(., 'Log out')]")


