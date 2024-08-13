from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
import time

@given('the Tunki app is opened')
def step_impl(context):
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='emulator-5554',
        app="C:\\Users\\cti23424\\Downloads\\presentation-qa.apk",
        language='en',
        locale='US'
    )
    appium_server_url = 'http://localhost:4724'
    context.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    time.sleep(8)

@when('I allow the notification permission if prompted')
def step_impl(context):
    try:
        el = context.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Allow"]')
        el.click()
    except Exception as e:
        print(f"Permission not required: {e}")
    time.sleep(3)

@when('I click on the "Login" button')
def step_impl(context):
    el = context.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("pe.indigital.tunki.user.qa:id/btn_login")')
    el.click()
    time.sleep(2)

@when('I enter my mobile number as "{number}"')
def step_impl(context, number):
    el = context.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Celular")')
    el.click()
    el.send_keys(number)

@when('I accept the entered mobile number')
def step_impl(context):
    el = context.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.LinearLayout").instance(0)')
    el.click()

@when('I enter my password using the on-screen keypad')
def step_impl(context):
    el = context.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Clave (6 dígitos)\")")
    el.click()
    digits = ['1', '5', '9', '6', '3', '2']
    for digit in digits:
        el = context.driver.find_element(by=AppiumBy.ID, value=f'pe.indigital.tunki.user.qa:id/btn_{digit}')
        el.click()

@then('I should see an error message displayed')
def step_impl(context):
    el = context.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/agora_x_error_text_view")
    el.click()