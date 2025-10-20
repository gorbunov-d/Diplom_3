from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Open path: {path}")
    def open(self, path: str = "/"):
        self.driver.get(f"{self.base_url}{path}")
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.accept_cookies()
        self.close_all_modals()

    @allure.step("Click element")
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

    @allure.step("Type text")
    def type(self, locator: tuple[By, str], text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        el.clear()
        el.send_keys(text)

    @allure.step("Wait visible")
    def visible(self, locator: tuple[By, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Exists check")
    def exists(self, locator: tuple[By, str]):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Press ESC")
    def press_escape(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    @allure.step("Accept cookies if present")
    def accept_cookies(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[contains(., 'Принять') or contains(., 'Accept') or contains(., 'Ясно')]")
            self.driver.execute_script("arguments[0].click();", btn)
        except Exception:
            pass

    @allure.step("Close all modals if present")
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

    def current_path(self) -> str:
        try:
            return self.driver.current_url.replace(self.base_url, "")
        except Exception:
            return ""

    @allure.step("Wait URL contains: {part}")
    def wait_url_contains(self, part: str):
        self.wait.until(lambda d: part in d.current_url)
