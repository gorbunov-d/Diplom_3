from selenium.webdriver.common.by import By


COUNTER_TOTAL = (By.CSS_SELECTOR, "[data-test='counter-total'], [class*='totalCounter']")
COUNTER_TODAY = (By.CSS_SELECTOR, "[data-test='counter-today'], [class*='todayCounter']")
FIRST_ORDER = (By.CSS_SELECTOR, "a[href*='/feed/']:not([href$='/feed'])")
ORDER_MODAL = (By.CSS_SELECTOR, "[data-order-modal], [role='dialog']")



