import os
import pytest
import requests
from utils.driver_factory import create_driver
from utils.urls import BASE_URL, AUTH_REGISTER, AUTH_LOGIN, AUTH_USER
from utils.helpers import random_credentials


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.getenv("BROWSER", "chrome"))
    parser.addoption("--headless", action="store_true", default=os.getenv("HEADLESS", "false").lower() == "true")


# base_url не как фикстура: импортируйте BASE_URL из utils.urls в тестах/страницах


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drv = create_driver(browser, headless)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_user():
    # Предусловие: регистрируем и логиним пользователя
    creds = random_credentials()
    requests.post(AUTH_REGISTER, json=creds)
    login = requests.post(AUTH_LOGIN, json={"email": creds["email"], "password": creds["password"]})
    token = login.json().get("accessToken", "") if login.ok else ""
    yield creds
    if token:
        try:
            requests.delete(AUTH_USER, headers={"Authorization": token})
        except Exception:
            pass


@pytest.fixture
def authorized_session():
    # Регистрируем/логиним и возвращаем токены вместе с кредами
    creds = random_credentials()
    requests.post(AUTH_REGISTER, json=creds)
    login = requests.post(AUTH_LOGIN, json={"email": creds["email"], "password": creds["password"]})
    body = login.json() if login.ok else {}
    tokens = {"accessToken": body.get("accessToken", ""), "refreshToken": body.get("refreshToken", "")}
    yield {"creds": creds, "tokens": tokens}
    if tokens.get("accessToken"):
        try:
            requests.delete(AUTH_USER, headers={"Authorization": tokens["accessToken"]})
        except Exception:
            pass


@pytest.fixture
def web_authorized_session(driver, authorized_session):
    # Прокидываем токены в localStorage и обновляем страницу
    driver.get(BASE_URL)
    access = authorized_session["tokens"].get("accessToken", "")
    refresh = authorized_session["tokens"].get("refreshToken", "")
    driver.execute_script("window.localStorage.setItem('accessToken', arguments[0]);", access)
    driver.execute_script("window.localStorage.setItem('refreshToken', arguments[0]);", refresh)
    driver.refresh()
    return authorized_session
