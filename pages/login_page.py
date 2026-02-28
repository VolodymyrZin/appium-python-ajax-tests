from appium_python_ajax_tests.pages import Page
import time
import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
PASSWORD_WRONG = os.getenv("PASSWORD_WRONG")
NAME = os.getenv("NAME")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' was executed in {end - start:.4f} sec")
        return result
    return wrapper

class LoginPage(Page):

    def __init__(self) -> None:
        super().__init__()

        self.login_input_id = 'authLoginEmail'
        self.password_input_id = 'authLoginPassword'
        self.login_button_id = 'authLogin'
        self.login_page_back_button_id = 'back'

    def login(self) -> None:
        login_input_xpath = self.get_input_field_xpath(self.login_input_id)
        login_input_field = self.find_element_by_xpath(login_input_xpath)
        self.send_keys(login_input_field, LOGIN)

        password_input_xpath = self.get_input_field_xpath(self.password_input_id)
        password_input_field = self.find_element_by_xpath(password_input_xpath)
        self.send_keys(password_input_field, PASSWORD)

        login_button = self.find_element_by_id(self.login_button_id)
        login_button.click()

    @timer
    def login_negative(self) -> None:
        login_input_xpath = self.get_input_field_xpath(self.login_input_id)
        login_input_field = self.find_element_by_xpath(login_input_xpath)
        self.send_keys(login_input_field, LOGIN)

        password_input_xpath = self.get_input_field_xpath(self.password_input_id)
        password_input_field = self.find_element_by_xpath(password_input_xpath)
        self.send_keys(password_input_field, PASSWORD_WRONG)

        login_button = self.find_element_by_id(self.login_button_id)
        login_button.click()

    def click_login_page_back_button(self):
        login_page_back_button = self.find_element_by_id(self.login_page_back_button_id)
        login_page_back_button.click()

