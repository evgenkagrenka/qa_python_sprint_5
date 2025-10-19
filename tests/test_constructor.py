from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import data 
import locators 
import curl

#проверка перехода к разделам конструктора

class TestConstructor:

    @pytest.mark.parametrize("button,text", [
        (locators.Button.SAUCES, locators.Text.TEXT_SAUCES),
        (locators.Button.BUNS, locators.Text.TEXT_BUNS),
        (locators.Button.FILLINGS, locators.Text.TEXT_FILLINGS)
    ])
    def test_constructor_tabs(self, authorized_driver, button, text):
        driver = authorized_driver

        # arrange
       
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))


        if driver.find_element(*locators.Text.TEXT_BUNS):
            driver.find_element(*locators.Button.SAUCES).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locators.Text.TEXT_SAUCES)
            )
            driver.find_element(*locators.Button.BUNS).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locators.Text.TEXT_BUNS)
            )

        # act
        driver.find_element(*button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(text))


        # assert
        assert driver.find_element(*text).is_displayed()
