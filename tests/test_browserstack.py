
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have
from selene.support.shared import browser
from allure import step


def test_search(driver_management):
    with step("Type search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")

    with step("Verify content found"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_article(driver_management):
    with step("Upload page of Wikipedia"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with step("Type text"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Moscow")

    with step("Assert the numbers of results"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))