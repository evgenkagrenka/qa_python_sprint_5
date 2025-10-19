from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data 
import locators 
import curl

#проверка авторизации пользователя по кнопке войти в аккаунт на главной странице
class TestAuthorizationFromMainPage:

    def test_success_authorization_from_main_page(self, driver):
         #arrange
        driver.get(curl.main_site)
        driver.find_element(*locators.Button.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))
        driver.find_element(*locators.Field.EMAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.registered_user['password'])
        #act
        driver.find_element(*locators.Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))
        #assert
        assert driver.current_url == curl.main_site

#проверка авторизации пользователя по кнопке войти на странице личного кабинета
class TestAuthorizationFromPersonalAccountPage:

    def test_success_authorization_from_personal_account_page(self, driver):
         #arrange
        driver.get(curl.main_site)

        driver.find_element(*locators.Button.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))
        driver.find_element(*locators.Field.EMAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.registered_user['password'])
        #act
        driver.find_element(*locators.Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))
        #assert
        assert driver.current_url == curl.main_site

#проверка авторизации пользователя с формы регистрации
class TestAuthorizationFromRegistrationPage:

    def test_success_authorization_from_registration_page(self, driver):
         #arrange
        driver.get(curl.registration)
        driver.find_element(*locators.Text.LOGIN_IN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))
        driver.find_element(*locators.Field.EMAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.registered_user['password'])
        #act
        driver.find_element(*locators.Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))
        #assert
        assert driver.current_url == curl.main_site

#проверка авторизации пользователя со страницы восстановления пароля
class TestAuthorizationFromPasswordRecoveryPage:

    def test_success_authorization_from_password_recovery_page(self, driver):
         #arrange
        driver.get(curl.pass_rec)
        driver.find_element(*locators.Text.LOGIN_IN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.pers_acc))
        driver.find_element(*locators.Field.EMAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*locators.Field.PASSWORD).send_keys(data.registered_user['password'])
        #act
        driver.find_element(*locators.Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))
        #assert
        assert driver.current_url == curl.main_site