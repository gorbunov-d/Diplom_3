import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

BASE_URL = os.getenv("SB_BASE_URL", "https://stellarburgers.education-services.ru").rstrip("/")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "debug")
os.makedirs(OUT_DIR, exist_ok=True)


def save(driver, name: str):
    html = driver.execute_script("return document.documentElement.outerHTML;")
    with open(os.path.join(OUT_DIR, f"{name}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    driver.save_screenshot(os.path.join(OUT_DIR, f"{name}.png"))


def main():
    opts = ChromeOptions()
    opts.add_argument("--window-size=1440,1000")
    # headed on purpose
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(BASE_URL + "/")
        save(driver, "main")
        # Open login
        driver.get(BASE_URL + "/login")
        save(driver, "login")
        # Open forgot
        driver.get(BASE_URL + "/forgot-password")
        save(driver, "forgot")
        # Open feed
        driver.get(BASE_URL + "/feed")
        save(driver, "feed")
        # Open profile (without auth just to capture layout)
        driver.get(BASE_URL + "/account/profile")
        save(driver, "profile")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

