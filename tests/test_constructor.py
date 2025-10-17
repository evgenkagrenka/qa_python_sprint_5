from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
from locators import TestLocators
import curl

#проверка перехода к разделам конструктора
class TestConstructor:

   def test_constructor(self, authorized_driver):
        
        # arrange
        driver = authorized_driver
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

        # act
        driver.find_element(*TestLocators.SAUCES).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Соусы']")))
        driver.find_element(*TestLocators.BUNS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Булки']")))
        driver.find_element(*TestLocators.FILLINGS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Начинки']")))

        # assert
        assert driver.find_element(By.XPATH, "//h2[text() = 'Соусы']").is_displayed()
        assert driver.find_element(By.XPATH, "//h2[text() = 'Булки']").is_displayed()
        assert driver.find_element(By.XPATH, "//h2[text() = 'Начинки']").is_displayed()

 