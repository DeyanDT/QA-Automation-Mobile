from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


def login(wait):
    username = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        )
    )

    password = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        )
    )

    login_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
        )
    )

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    product_page = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("PRODUCTS")')
        )
    )

    assert product_page.is_displayed()