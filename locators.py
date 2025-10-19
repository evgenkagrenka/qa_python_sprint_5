from selenium.webdriver.common.by import By


class Button: # Локаторы кнопок

    # Локатор кнопки зарегистрироваться
    REG_BUTTON = By.XPATH, "//button[text() = 'Зарегистрироваться']"

    # Локатор кнопки войти в аккаунт на главной странице
    LOGIN_IN_ACCOUNT = By.XPATH, "//button[text() = 'Войти в аккаунт']"

    # Локатор кнопки войти
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"

    # Локатор кнопки выйти
    EXIT_BUTTON = By.XPATH, "//button[text() = 'Выход']"

    # Локатор кнопки Личный кабинет
    PERSONAL_ACCOUNT = By.XPATH, "//p[text() = 'Личный Кабинет']"

    # Локатор кнопки Логотипа
    LOGO = By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']"

    # Локатор кнопки Конструктор
    CONSTRUCTOR = By.XPATH, "//p[text() = 'Конструктор']"

    # Локатор в конструкторе "Булки"
    BUNS = By.XPATH, "//span[text() = 'Булки']"
    
    # Локатор в конструкторе "Соусы"
    SAUCES = By.XPATH, "//span[text() = 'Соусы']"
    
    # Локатор в конструкторе "Начинки"
    FILLINGS = By.XPATH, "//span[text() = 'Начинки']"


class Field: # Локаторы полей 

    # Локатор поля имя
    NAME = By.XPATH, "//label[text() = 'Имя']/parent::div/input"

    # Локатор поля е-маил
    EMAIL = By.XPATH, "//label[text() = 'Email']/parent::div/input"

    # Локатор поля пароль
    PASSWORD = By.XPATH, "//input[@type='password']"


class Text: # Локаторы надписей 

    # Локатор надписи Войти 
    LOGIN_IN = By.XPATH, "//a[text() = 'Войти']"
    
    # Локатор некорректного пароля
    INCORRECT_PASSWORD = By.XPATH, "//p[text() = 'Некорректный пароль']"

    #Локатор текста Булки, Соусы, Начинки в конструкторе
    TEXT_BUNS = By.XPATH, "//h2[text() = 'Булки']"

    TEXT_SAUCES = By.XPATH, "//h2[text() = 'Соусы']"

    TEXT_FILLINGS = By.XPATH, "//h2[text() = 'Начинки']"


    
    
    
    
  



