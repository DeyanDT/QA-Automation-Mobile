from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from helpers import login


def test_homepage_product_addCart(driver, wait):
    login(wait)


    add_to_cart_button = wait.until(
    EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//*[@text="Sauce Labs Bike Light"]'
            '/ancestor::*[@content-desc="test-Item"]'
            '//*[@content-desc="test-ADD TO CART"]'
        )
    )
)

    add_to_cart_button.click()

    cart = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Cart")))
    cart.click()

    checkout_button = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")))
    checkout_button.click()

    first_name = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-First Name")))
    last_name = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    postal_code = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")

    first_name.send_keys("Test")
    last_name.send_keys("User")
    postal_code.send_keys("12345")

    continue_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    continue_button.click()

    finish_button = wait.until(
    EC.element_to_be_clickable(
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().description("test-FINISH"))'
        )
    )
)

    finish_button.click()