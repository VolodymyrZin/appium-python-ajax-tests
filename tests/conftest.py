# from builtins import function

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from appium_python_ajax_tests.pages import IntroPage, LoginPage, MainPage, AppMenuPage, SettingsPage
from appium_python_ajax_tests.framework.appium import Appium
from appium_python_ajax_tests.framework.driver import Driver
from appium_python_ajax_tests.android_utils import get_driver_options, reset_app


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption('--login', action='store_true', default=False, help='Reset app and login before tests session')


def login() -> None:
    reset_app(Driver.app_package)
    Driver.launch_app()
    Driver.grant_application_permissions()

    IntroPage().click_login_button()
    LoginPage().login()

@pytest.fixture(scope='session')
def appium_service():
    # Перевіряємо, що Appium запущений
    if not Appium.is_running():
        raise RuntimeError(
            f"Appium не запущений на {Appium.HOST}:{Appium.PORT}. "
            "Запусти Appium вручну: appium --base-path /wd/hub"
        )
    yield

# @pytest.fixture(scope='session')
# def appium_service():
#     Appium.start()
#     yield
#     Appium.stop()


@pytest.fixture(scope='session', autouse=True)
def driver(appium_service, request: pytest.FixtureRequest):
    Driver.start(get_driver_options())
    if request.config.option.login:
        login()
    else:
        Driver.terminate_app()
        Driver.launch_app()
    yield
    Driver.finish()

@pytest.fixture(autouse=True)
def handle_permissions():
    try:
        Driver.appium_instance.find_element(
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button"
        ).click()
    except Exception:
        pass

@pytest.fixture()
def loginin():
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
    IntroPage().click_login_button()
    LoginPage().login()
    yield
    MainPage().click_burger_menu()
    AppMenuPage().click_app_settings_button()
    SettingsPage().click_logout_button()

@pytest.fixture()
def logout():
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
    IntroPage().click_login_button()
    LoginPage().login()

    MainPage().click_burger_menu()
    AppMenuPage().click_app_settings_button()
    SettingsPage().click_logout_button()
    yield