from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from helpers import login


def test_scrolling_and_click(driver, wait):
    login(wait)

    product = wait.until(
        EC.presence_of_element_located(
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("Test.allTheThings() T-Shirt (Red)"))'
            )
        )
    )

    assert product.is_displayed()
    product.click()

    product_title = wait.until(
        EC.visibility_of_element_located(
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("This classic Sauce Labs t-shirt")'
            )
        )
    )

    assert product_title.is_displayed()