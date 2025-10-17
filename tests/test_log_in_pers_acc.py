from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
from locators import TestLocators
import curl

#проверка перехода в личный кабинет авторизованного пользователя
class TestLogInPersAcc:

   def test_log_in_personal_account(self, authorized_driver):
        
        driver = authorized_driver

        # act
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.account))

        # assert
        assert driver.current_url == curl.account