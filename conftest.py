import pytest
import curl
import data
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# используемые фикстуры

@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

  
@pytest.fixture

def authorized_driver(driver):
    driver.get(curl.pers_acc)

    # Вводим данные пользователя
    driver.find_element(*TestLocators.EMAIL).send_keys(data.registered_user['e-mail'])
    driver.find_element(*TestLocators.PASSWORD).send_keys(data.registered_user['password'])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()

    # Возвращаем уже авторизованный драйвер
    return driver