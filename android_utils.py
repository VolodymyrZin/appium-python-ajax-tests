import os
import subprocess
from appium.options.android import UiAutomator2Options

# Беремо UDID з змінної оточення
udid = os.getenv("DEVICE_UDID")
if not udid:
    raise EnvironmentError(
        "No DEVICE_UDID provided. Set DEVICE_UDID=emulator-5554 або інший UDID вашого пристрою"
    )

def get_driver_options() -> UiAutomator2Options:
    options = UiAutomator2Options()

    options.new_command_timeout = 120
    options.unicode_keyboard = True
    options.reset_keyboard = True

    options.no_reset = False
    options.full_reset = False
    # options.no_reset = True
    options.udid = udid
    options.clear_device_logs_on_start = True
    options.auto_grant_permissions = True
    options.disable_window_animation = True
    return options

def reset_app(package: str) -> None:
    # Використовуємо ADB через UDID
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# import subprocess
#
# from appium.options.android import UiAutomator2Options
#
#
# adb_output = subprocess.getoutput('adb devices')
# if not adb_output or len(adb_output.splitlines()) == 1:
#     raise EnvironmentError('No Android device found')
# else:
#     udid = adb_output.splitlines()[1].split()[0]
#
#
# def get_driver_options() -> UiAutomator2Options:
#     options = UiAutomator2Options()
#     options.no_reset = True
#     options.udid = udid
#     options.clear_device_logs_on_start = True
#     options.auto_grant_permissions = True
#     options.disable_window_animation = True
#     return options
#
#
# def reset_app(package) -> None:
#     subprocess.run(
#         ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
#         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#     )
