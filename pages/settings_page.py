from appium_python_ajax_tests.pages import Page

class SettingsPage(Page):
    def __init__(self) -> None:
        super().__init__()
        self.logout_button_id = 'accountInfoLogoutNavigate'
        self.edit_button_id = 'accountInfoEditAccountNavigate'
        self.changed_name_id = 'title'

    def click_logout_button(self) -> None:
        logout_button = self.find_element_by_id(self.logout_button_id)
        logout_button.click()

    def click_edit_account_button(self) -> None:
        edit_button = self.find_element_by_id(self.edit_button_id)
        edit_button.click()

