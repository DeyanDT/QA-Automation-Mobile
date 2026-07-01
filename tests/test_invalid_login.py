from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login(driver, wait):
    username = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
    password = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    username.send_keys("user")
    password.send_keys("pass")
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Error message")))
    assert error_message.is_displayed()