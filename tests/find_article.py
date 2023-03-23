import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have
from selene.support.shared import browser



options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",

    # Set URL of the application under test
    "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "QA QURU Project",
        "buildName" : "browserstack-build-HW",
        "sessionName" : "BStack first_test",

        # Set your access credentials
        "userName" : "kseniiatrepp_p47KJy",
        "accessKey" : "gKFApk5KGGC4cMx72VAC"
    }
})

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
with allure.step("Uplode page of Wikipedia"):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

with allure.step("Type text"):
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Moscow")

with allure.step("Assert the numbers of results"):
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

# Invoke driver.quit() after the test is done to indicate that the test is completed.
browser.quit()