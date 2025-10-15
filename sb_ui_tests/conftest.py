import os
import pytest
import requests
from utils.driver_factory import create_driver

BASE_URL = os.getenv("SB_BASE_URL", "https://stellarburgers.education-services.ru").rstrip("/")
API_BASE = os.getenv("SB_API_URL", "https://stellarburgers.education-services.ru").rstrip("/")


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.getenv("BROWSER", "chrome"))
    parser.addoption("--headless", action="store_true", default=os.getenv("HEADLESS", "false").lower() == "true")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drv = create_driver(browser, headless)
    yield drv
    drv.quit()


@pytest.fixture
def user_credentials():
    import random, string
    def rnd(n=8):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(n))
    email = f"{rnd()}@example.com"
    password = rnd(12)
    name = rnd(6)
    return {"email": email, "password": password, "name": name}


@pytest.fixture
def logged_in_user(user_credentials):
    reg = requests.post(f"{API_BASE}/api/auth/register", json=user_credentials)
    assert reg.status_code in (200, 403)
    login = requests.post(f"{API_BASE}/api/auth/login", json={"email": user_credentials["email"], "password": user_credentials["password"]})
    assert login.status_code == 200
    token = login.json().get("accessToken", "")
    yield user_credentials
    if token:
        try:
            requests.delete(f"{API_BASE}/api/auth/user", headers={"Authorization": token})
        except Exception:
            pass


@pytest.fixture
def login_tokens(user_credentials):
    reg = requests.post(f"{API_BASE}/api/auth/register", json=user_credentials)
    assert reg.status_code in (200, 403)
    login = requests.post(f"{API_BASE}/api/auth/login", json={"email": user_credentials["email"], "password": user_credentials["password"]})
    assert login.status_code == 200
    body = login.json()
    tokens = {"accessToken": body.get("accessToken", ""), "refreshToken": body.get("refreshToken", "")}
    yield {"creds": user_credentials, "tokens": tokens}
    if tokens.get("accessToken"):
        try:
            requests.delete(f"{API_BASE}/api/auth/user", headers={"Authorization": tokens["accessToken"]})
        except Exception:
            pass


@pytest.fixture
def authorized_session(driver, base_url, login_tokens):
    driver.get(base_url)
    access = login_tokens["tokens"].get("accessToken", "")
    refresh = login_tokens["tokens"].get("refreshToken", "")
    driver.execute_script("window.localStorage.setItem('accessToken', arguments[0]);", access)
    driver.execute_script("window.localStorage.setItem('refreshToken', arguments[0]);", refresh)
    driver.refresh()
    return login_tokens
