import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser: str | None = None, headless: bool | None = None):
    browser = (browser or os.getenv("BROWSER", "chrome")).lower()
    headless = headless if headless is not None else os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        driver = webdriver.Chrome(options=options)
        return driver

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1280, 900)
        return driver

    raise ValueError(f"Unsupported browser: {browser}")

