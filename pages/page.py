from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_python_ajax_tests.framework.logger import logger


from appium_python_ajax_tests.framework.driver import Driver


class Page:

    TIMEOUT = 30

    def find_element_by_id(self, element_id: str):
        resource_id = self._get_resource_id(element_id)
        logger.info(f"Searching element by id: {resource_id}")
        return self._wait_for_element(AppiumBy.ID, resource_id)

    def find_element_by_xpath(self, xpath: str):
        return self._wait_for_element(AppiumBy.XPATH, xpath)

    @classmethod
    def _wait_for_element(cls, strategy: str, selector: str):
        return WebDriverWait(Driver.appium_instance, cls.TIMEOUT).until(
            expected_conditions.presence_of_element_located((strategy, selector))
        )

    @staticmethod
    def send_keys(element: WebElement, value: str) -> None:
        element.clear().send_keys(value)

    @staticmethod
    def _get_resource_id(element_id: str) -> str:
        return f'{Driver.app_package}:id/{element_id}'

    def wait_until_element_is_visible(self, selector: str):
        Driver.appium_instance.wait_activity("com.ajaxsystems.MainActivity", 10)
        return WebDriverWait(Driver.appium_instance, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, selector)))

    def get_input_field_xpath(self, resource_id: str) -> str:
        resource_id = self._get_resource_id(resource_id)
        return f'//android.widget.EditText[@resource-id="{resource_id}"]'