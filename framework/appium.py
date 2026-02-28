from appium.webdriver.appium_service import AppiumService

import os
from appium.webdriver.appium_service import AppiumService

class Appium:
    service = None
    HOST = os.getenv("APPIUM_HOST", "http://localhost")
    PORT = os.getenv("APPIUM_PORT", "4723")

    @classmethod
    def start(cls) -> None:
        # запуск Appium тільки локально (не у Docker)
        if os.getenv("DOCKER", "0") == "1":
            return
        cls.service = AppiumService()
        cls.service.start(args=['-a', cls.HOST, '-p', cls.PORT, '--relaxed-security', '--allow-insecure', 'adb_shell'])

    @classmethod
    def stop(cls) -> None:
        if os.getenv("DOCKER", "0") == "1" or not cls.service:
            return
        cls.service.stop()

# class Appium:
#     service = AppiumService()
#     HOST = '127.0.0.1'
#     PORT = '4723'
#
#     @classmethod
#     def start(cls) -> None:
#         cls.service.start(
#             args=['-a', cls.HOST, '-p', cls.PORT, '--relaxed-security', '--allow-insecure', 'adb_shell']
#         )
#
#     @classmethod
#     def stop(cls) -> None:
#         cls.service.stop()
