from appium_python_ajax_tests.pages.page import Page

class AppMenuPage(Page):
    def __init__(self) -> None:
        super().__init__()

        self.app_settings_button_id = 'settings'

    def click_app_settings_button(self) -> None:
        settings_button = self.find_element_by_id(self.app_settings_button_id)
        settings_button.click()