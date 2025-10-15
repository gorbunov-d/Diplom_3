from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, 20)

    def open(self, path: str = "/"):
        self.driver.get(f"{self.base_url}{path}")
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.accept_cookies()
        self.close_all_modals()

    def click(self, locator: tuple[By, str]):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            try:
                el.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator: tuple[By, str], text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        el.clear()
        el.send_keys(text)

    def visible(self, locator: tuple[By, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def exists(self, locator: tuple[By, str]):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    def press_escape(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    def accept_cookies(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[contains(., 'Принять') or contains(., 'Accept') or contains(., 'Ясно')]")
            self.driver.execute_script("arguments[0].click();", btn)
        except Exception:
            pass

    def close_all_modals(self):
        try:
            close_btns = self.driver.find_elements(By.CSS_SELECTOR, ".Modal_modal__P3_V5 button")
            for btn in close_btns:
                try:
                    self.driver.execute_script("arguments[0].click();", btn)
                except Exception:
                    pass
        except Exception:
            pass
