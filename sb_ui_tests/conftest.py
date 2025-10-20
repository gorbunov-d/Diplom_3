import os
import pytest
import requests
from utils.driver_factory import create_driver
from utils.urls import BASE_URL, AUTH_REGISTER, AUTH_LOGIN, AUTH_USER


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.getenv("BROWSER", "chrome"))
    parser.addoption("--headless", action="store_true", default=os.getenv("HEADLESS", "false").lower() == "true")


@pytest.fixture(scope="session")
def base_url():
    # Простая фикстура для базового URL. Значение берём из data-модуля.
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
    from utils.helpers import random_credentials
    return random_credentials()


@pytest.fixture
def logged_in_user(user_credentials):
    # Предусловие: регистрируем и логиним пользователя; без assert, ошибки поймает тест
    requests.post(AUTH_REGISTER, json=user_credentials)
    login = requests.post(AUTH_LOGIN, json={"email": user_credentials["email"], "password": user_credentials["password"]})
    token = login.json().get("accessToken", "") if login.ok else ""
    try:
        yield user_credentials
    finally:
        if token:
            try:
                requests.delete(AUTH_USER, headers={"Authorization": token})
            except Exception:
                pass


@pytest.fixture
def login_tokens(user_credentials):
    requests.post(AUTH_REGISTER, json=user_credentials)
    login = requests.post(AUTH_LOGIN, json={"email": user_credentials["email"], "password": user_credentials["password"]})
    body = login.json() if login.ok else {}
    tokens = {"accessToken": body.get("accessToken", ""), "refreshToken": body.get("refreshToken", "")}
    try:
        yield {"creds": user_credentials, "tokens": tokens}
    finally:
        if tokens.get("accessToken"):
            try:
                requests.delete(AUTH_USER, headers={"Authorization": tokens["accessToken"]})
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
