import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():

    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:udid": "emulator-5554",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:noReset": False,
        "appium:dontStopAppOnReset": True
    }

    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver

    driver.quit()

@pytest.fixture
def wait(driver):
        return WebDriverWait(driver, 10)