import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app="C:\\Users\\cti23424\\Downloads\\presentation-qa.apk",
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4724'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_open_app(self) -> None:
        time.sleep(8)
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Allow"]')
            el.click()
        except Exception as e:
            print(f"No existe notificacion: {e}")

        #el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="pe.indigital.tunki.user.qa:id/btn_login"]')
        #el.click()

        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"pe.indigital.tunki.user.qa:id/btn_login\")")
        el.click()
        time.sleep(3)
        #Seleccion el celular e ingreso los valores
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Celular\")")
        el.click()
        #Ingreso los valores
        el.send_keys("030345612")
        #Acepto los datos enviados
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.LinearLayout\").instance(0)")
        el.click()
        #Ingreso contraseña
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Clave (6 dígitos)\")")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_1")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_5")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_9")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_6")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_3")
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_2")
        el.click()

        #Loguearse
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/btn_login")
        el.click()
        time.sleep(5)
        #Validar mensaje de error
        el = self.driver.find_element(by=AppiumBy.ID, value="pe.indigital.tunki.user.qa:id/agora_x_error_text_view")
        el.click()

if __name__ == '__main__':
    unittest.main()

