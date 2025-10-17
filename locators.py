from selenium.webdriver.common.by import By


class TestLocators:

    # Локатор кнопки зарегестрироваться
    REG_BUTTON =By.XPATH, "//button[text() = 'Зарегистрироваться']"
    
    # Локатор поля имя
    NAME = By.XPATH, "//label[text() = 'Имя']/parent::div/input"

    # Локатор поля е-маил
    EMAIL = By.XPATH, "//label[text() = 'Email']/parent::div/input"

    # Локатор поля пароль
    PASSWORD = By.XPATH, "//input[@type='password']"

    # Локатор кнопки войти
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"

    # Локатор надписи Войти 
    LOGIN_IN = By.XPATH, "//a[text() = 'Войти']"
    
    # Локатор кнопки войти в аккаунт на главной странице
    LOGIN_IN_ACCOUNT = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    
    # Локатор некорректного пароля
    INCORRECT_PASSWORD = By.XPATH, "//p[text() = 'Некорректный пароль']"
    
    # Локатор кнопки выйти
    EXIT_BUTTON = By.XPATH, "//button[text() = 'Выход']"
    
    # Локатор в конструкторе "Булки"
    BUNS = By.XPATH, "//span[text() = 'Булки']"
    
    # Локатор в конструкторе "Соусы"
    SAUCES = By.XPATH, "//span[text() = 'Соусы']"
    
    # Локатор в конструкторе "Начинки"
    FILLINGS = By.XPATH, "//span[text() = 'Начинки']"
    
    # Локатор кнопки Личный кабинет
    PERSONAL_ACCOUNT = By.XPATH, "//p[text() = 'Личный Кабинет']"
    
    # Локатор кнопки Конструктор
    CONSTRUCTOR = By.XPATH, "//p[text() = 'Конструктор']"
    
    # Локатор кнопки Логотипа
    LOGO = By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']"

