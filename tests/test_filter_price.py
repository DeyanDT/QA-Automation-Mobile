from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from helpers import login

def test_filter(driver, wait):
    login(wait)

    filter_button = wait.until(
    EC.visibility_of_element_located(
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.ImageView").instance(5)'
        )
    )
)
    filter_button.click()


    sort_option = wait.until(EC.visibility_of_element_located(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Price (low to high)")')))
    sort_option.click()

    price_elements = driver.find_elements(
    AppiumBy.ACCESSIBILITY_ID,
    "test-Price"
)

    prices = [float(el.text.replace("$", "")) for el in price_elements]

    assert prices == sorted(prices)