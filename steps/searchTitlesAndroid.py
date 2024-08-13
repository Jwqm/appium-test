from behave import given, when, then
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4724'

@given('open menu')
def open_menu(self):
    self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    
@when('select settings')
def select_settings(context):
    print('open')

@then('verify title "{title}" and close')
def verify_title_apps_and_open(self, title):
    el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="' + title + '"]')
    el.click()
    time.sleep(3)
    self.driver.quit()

