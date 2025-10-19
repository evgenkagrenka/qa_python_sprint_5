from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
import locators
import curl

#проверка регистрации пользователя с валидными данными
class TestRegistrationValid:

    def test_success_registration(self, driver):
         #arrange
        driver.get(curl.registration)
        driver.find_element(*locators.Field.NAME).send_keys(data.new_correct_user['name'])
        driver.find_element(*locators.Field.EMAIL).send_keys(data.new_correct_user['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.new_correct_user['password'])
        #act
        driver.find_element(*locators.Button.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))
        #assert
        assert driver.current_url == curl.pers_acc

#проверка регистрации пользователя с невалидным паролем (меньше 6 символов)
class TestRegistrationInvalid:

    def test_registration_with_short_password(self, driver):
         #arrange
        driver.get(curl.registration)
        driver.find_element(*locators.Field.NAME).send_keys(data.new_user_wrong_password['name'])
        driver.find_element(*locators.Field.EMAIL).send_keys(data.new_user_wrong_password['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.new_user_wrong_password['password'])
        #act
        driver.find_element(*locators.Button.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locators.Text.INCORRECT_PASSWORD))
        #assert
        assert driver.find_element(*locators.Text.INCORRECT_PASSWORD).text == data.incorrect_password_text