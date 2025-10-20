from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
import locators
import curl

#проверка выхода из аккаунта
class TestLogOut:

   def test_log_out(self, authorized_driver):
        
        driver = authorized_driver

        # act
        driver.find_element(*locators.Button.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.account))
        driver.find_element(*locators.Button.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))

        # assert
        assert driver.current_url == curl.pers_acc