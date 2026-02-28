from appium_python_ajax_tests.pages import Page
# from appium_python_ajax_tests.credentials import LOGIN, PASSWORD, PASSWORD_WRONG, NAME
from appium_python_ajax_tests.pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
PASSWORD_WRONG = os.getenv("PASSWORD_WRONG")
NAME = os.getenv("NAME")

class EditAccountPage(Page):
    def __init__(self) -> None:
        super().__init__()
        self.delete_account_id = 'userDeleteAccount'
        self.name_input_id = 'accountSettingsName'
        self.back_button_id = 'back'


    def input_name_field(self) -> None:

        name_field__button = self.find_element_by_id(self.name_input_id)
        name_field__button.click()

    # def change_name(self) -> None:
    #     name_input_xpath = self.get_input_field_xpath(self.name_input_id)
    #     name_input_field = self.find_element_by_xpath(name_input_xpath)
    #     self.send_keys(name_input_field, NAME)

    def change_name(self, new_name: str) -> None:
        login_input_xpath = self.get_input_field_xpath(self.name_input_id)
        login_input_field = self.find_element_by_xpath(login_input_xpath)
        self.send_keys(login_input_field, new_name)

    def click_back_button(self):
        back_button = self.find_element_by_id(self.back_button_id)
        back_button.click()