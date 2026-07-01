from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from helpers import login

def test_add_product_profile_to_cart(driver, wait):
    login(wait)

    product = wait.until(EC.visibility_of_element_located(
     (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")')))
    
    product.click()
    
    wait.until(
    EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "test-Inventory item page")
    )
)

    add_to_cart_button = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.scrollIntoView(new UiSelector().description("test-ADD TO CART"))'
)
    add_to_cart_button.click()

    cart_button = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "test-Cart")))
    cart_button.click()

    product_in_cart = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")')))

    assert "Sauce Labs Backpack" in product_in_cart.text