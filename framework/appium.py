from appium.webdriver.appium_service import AppiumService

import os
import requests

class Appium:
    HOST = os.getenv("APPIUM_HOST", "http://localhost")
    PORT = os.getenv("APPIUM_PORT", "4723")

    @classmethod
    def is_running(cls) -> bool:
        url = f"{cls.HOST}:{cls.PORT}/wd/hub/status"
        try:
            r = requests.get(url, timeout=5)
            return r.status_code == 200
        except requests.RequestException:
            return False

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
