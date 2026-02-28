from contextlib import suppress
from selenium.common.exceptions import WebDriverException
from appium.webdriver import Remote
from appium.webdriver.appium_connection import AppiumConnection
from appium.options.android import UiAutomator2Options
from appium_python_ajax_tests.framework.appium import Appium
from appium_python_ajax_tests.android_utils import get_driver_options

class Driver:
    app_package = 'com.ajaxsystems'
    appium_instance = None

    @classmethod
    def start(cls, options: UiAutomator2Options | None = None) -> None:
        if options is None:
            options = get_driver_options()
        if not Appium.is_running():
            raise RuntimeError("Appium server is not running at {0}:{1}".format(Appium.HOST, Appium.PORT))
        cls.appium_instance = Remote(AppiumConnection(f"{Appium.HOST}:{Appium.PORT}/wd/hub"), options=options)

    @classmethod
    def finish(cls) -> None:
        cls.terminate_app()
        if cls.appium_instance:
            cls.appium_instance.quit()
        cls.appium_instance = None

    @classmethod
    def launch_app(cls) -> None:
        cls.appium_instance.activate_app(cls.app_package)

    @classmethod
    def terminate_app(cls) -> None:
        with suppress(WebDriverException):
            cls.appium_instance.terminate_app(cls.app_package)

    @classmethod
    def grant_application_permissions(cls) -> None:
        permissions = [
            'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE',
            'WRITE_EXTERNAL_STORAGE', 'CAMERA', 'READ_CONTACTS'
        ]
        platform_version = int(cls.appium_instance.capabilities['platformVersion'].split('.')[0])

        if platform_version >= 10:
            permissions.append('ACCESS_BACKGROUND_LOCATION')
        if platform_version >= 13:
            permissions.append('POST_NOTIFICATIONS')

        for permission in permissions:
            with suppress(WebDriverException):
                cls.appium_instance.execute_script(
                    'mobile: shell',
                    {'command': 'pm grant', 'args': [f'{cls.app_package} android.permission.{permission}']}
                )
# from contextlib import suppress
#
# from appium.options.android import UiAutomator2Options
# from appium.webdriver import Remote
# from appium.webdriver.appium_connection import AppiumConnection
# from selenium.common.exceptions import WebDriverException
#
# from appium_python_ajax_tests.framework.appium import Appium
#
#
# class Driver:
#     app_package = 'com.ajaxsystems'
#     appium_instance = None
#
#     @classmethod
#     def start(cls, options: UiAutomator2Options) -> None:
#         cls.appium_instance = Remote(AppiumConnection(f'{Appium.HOST}:{Appium.PORT}'), options=options)
#
#     @classmethod
#     def finish(cls) -> None:
#         cls.appium_instance.terminate_app(cls.app_package)
#         cls.appium_instance.quit()
#         cls.appium_instance = None
#
#     @classmethod
#     def launch_app(cls) -> None:
#         cls.appium_instance.activate_app(cls.app_package)
#
#     @classmethod
#     def terminate_app(cls) -> None:
#         with suppress(WebDriverException):
#             cls.appium_instance.terminate_app(cls.app_package)
#
#     @classmethod
#     def grant_application_permissions(cls) -> None:
#         permissions = [
#             'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE',
#             'WRITE_EXTERNAL_STORAGE', 'CAMERA', 'READ_CONTACTS'
#         ]
#         platform_version = cls.appium_instance.capabilities['platformVersion']
#
#         if int(platform_version) >= 10:
#             permissions.append('ACCESS_BACKGROUND_LOCATION')
#
#         if int(platform_version) >= 13:
#             permissions.append('POST_NOTIFICATIONS')
#
#         for permission in permissions:
#             with suppress(WebDriverException):
#                 cls.appium_instance.execute_script(
#                     'mobile: shell',
#                     {'command': 'pm grant', 'args': [f'{cls.app_package} android.permission.{permission}']}
#                 )
