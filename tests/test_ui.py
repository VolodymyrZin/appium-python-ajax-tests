from appium.webdriver.common.appiumby import AppiumBy
from appium_python_ajax_tests.framework.driver import Driver
from appium_python_ajax_tests.pages import Page, MainPage, IntroPage, LoginPage, AppMenuPage, SettingsPage, \
    EditAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
PASSWORD_WRONG = os.getenv("PASSWORD_WRONG")
NAME = os.getenv("NAME")


@pytest.mark.primary()
def test_start_login_page_isvisible():
    page = Page()
    page.wait_until_element_is_visible("com.ajaxsystems:id/authHelloLogin")

    assert Driver.appium_instance.find_element(
        AppiumBy.ID,
        "com.ajaxsystems:id/authHelloLogin"
    )


@pytest.mark.main()
def test_login(loginin):
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
    # IntroPage().click_login_button()
    # LoginPage().login()
    # Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)
    assert Driver.appium_instance.find_element(
        AppiumBy.ID,
        "com.ajaxsystems:id/controlImage"
    )
@pytest.mark.main()
def test_logout(logout):


# MainPage().click_burger_menu()
    # AppMenuPage().click_app_settings_button()
    # SettingsPage().click_logout_button()
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)
    assert Driver.appium_instance.find_element(
        AppiumBy.ID,
        "com.ajaxsystems:id/authHelloLogin"
    )
# def test_login(login_logout):
#     Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
#     # IntroPage().click_login_button()
#     # LoginPage().login()
#     Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)
#     assert Driver.appium_instance.find_element(
#         AppiumBy.ID,
#         "com.ajaxsystems:id/controlImage"
#     )
#     # MainPage().click_burger_menu()
#     # AppMenuPage().click_app_settings_button()
#     # SettingsPage().click_logout_button()
#     Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)
#     assert Driver.appium_instance.find_element(
#         AppiumBy.ID,
#         "com.ajaxsystems:id/authHelloLogin"
#     )


users_list = [
    {'first_name': 'Taras', 'last_name': 'Shevchenko', 'age': 47, 'hubs': {'Hub+', 'Hub', 'Hub2'}},
    {'first_name': 'Stepan', 'last_name': 'Bandera', 'age': 50, 'hubs': {'Hub2+', 'Hub+', 'Hub2'}},
    {'first_name': 'Ivan', 'last_name': 'Puluj', 'age': 72, 'hubs': {'Hub2+', 'Hub+', 'Hub', 'Hub2'}},
    {'first_name': 'Bohdan', 'last_name': 'Khmelnytsky', 'age': 61, 'hubs': {'Hub2+', 'Hub'}},
    {'first_name': 'Viacheslav', 'last_name': 'Chornovil', 'age': 61, 'hubs': {'Hub2', 'Hub Hybrid'}},
    {'first_name': 'Andriy', 'last_name': 'Kuzmenko', 'age': 46, 'hubs': {'Hub', 'Hub2'}}
]

# фільтрація користувачів
mod_users_list = [user for user in users_list if user['age'] > 50 and 'Hub2' in user['hubs']]

# ids для звіту
ids = [f"{u['first_name']} {u['last_name']}" for u in mod_users_list]


@pytest.mark.parametrize('user', mod_users_list, ids=ids)
@pytest.mark.change
def test_edit_name(user):
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
    IntroPage().click_login_button()
    LoginPage().login()
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)

    assert Driver.appium_instance.find_element(
        AppiumBy.ID,
        "com.ajaxsystems:id/controlImage"
    )

    MainPage().click_burger_menu()
    AppMenuPage().click_app_settings_button()
    SettingsPage().click_edit_account_button()

    # вводимо ім’я та прізвище користувача
    new_name = f"{user['first_name']} {user['last_name']}"
    EditAccountPage().change_name(new_name)
    EditAccountPage().click_back_button()

    namebar = WebDriverWait(Driver.appium_instance, 5).until(
        EC.visibility_of_element_located(
            (AppiumBy.ID, "com.ajaxsystems:id/title")
        )
    )

    # перевіряємо, що нове ім’я відображається
    assert new_name in namebar.text

    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 1)
    SettingsPage().click_logout_button()


@pytest.mark.negative()
def test_login_negative():
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 2)

    IntroPage().click_login_button()
    LoginPage().login_negative()

    snackbar = WebDriverWait(Driver.appium_instance, 5).until(
        EC.visibility_of_element_located(
            (AppiumBy.ID, "com.ajaxsystems:id/snackbar_text")
        )
    )
    assert "Wrong login/password combination" in snackbar.text
    LoginPage().click_login_page_back_button()


@pytest.mark.params()
def test_navbar_elements():
    main_page = MainPage()
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
    IntroPage().click_login_button()
    LoginPage().login()
    Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 5)

    navbar_dict = main_page.get_navbar_elements()
    # перевіряємо, що всі потрібні поля присутні
    assert "devicesTitle" in navbar_dict
    assert "roomsTitle" in navbar_dict
    assert "notificationsTitle" in navbar_dict
    assert "controlTitle" in navbar_dict

    # перевіряємо координати
    for text, coord in navbar_dict.items():
        print(f"{text} has coordinates {coord}")


def test_navbar_order():
    main_page = MainPage()
    navbar = main_page.get_navbar_elements()

    order = [
        "devicesTitle",
        "roomsTitle",
        "notificationsTitle",
        "controlTitle"
    ]

    xs = [navbar[item]["x"] for item in order]

    assert xs == sorted(xs)
    MainPage().click_burger_menu()
    AppMenuPage().click_app_settings_button()
    SettingsPage().click_logout_button()
