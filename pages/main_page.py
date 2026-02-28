from appium_python_ajax_tests.framework.logger import logger
from appium_python_ajax_tests.pages import Page


class MainPage(Page):
    def __init__(self) -> None:
        super().__init__()
        self.burger_menu_id = 'menuDrawer'

    def click_burger_menu(self):
        logger.info("Click burger menu")
        self.find_element_by_id(self.burger_menu_id).click()

    def get_navbar_elements(self) -> dict[str, dict[str, int]]:
        ids = [
            "devicesTitle",
            "roomsTitle",
            "notificationsTitle",
            "controlTitle"
        ]
        elements = [self.find_element_by_id(i) for i in ids]
        coords = [el.location for el in elements]
        return {i: coord for i, coord in zip(ids, coords)}
