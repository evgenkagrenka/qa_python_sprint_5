from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
from locators import TestLocators
import curl

#проверка перехода из личного кабинета в конструктор
class TestPersAccToConstructor:

   def test_pers_acc_to_constructor(self, authorized_driver):
        
        driver = authorized_driver

        # act
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

        # assert
        assert driver.current_url == curl.main_site

#проверка перехода из личного кабинета в конструктор по клику на логотип
   def test_pers_acc_to_constructor_by_logo(self, authorized_driver):
        
        driver = authorized_driver

        # act
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

        # assert
        assert driver.current_url == curl.main_site