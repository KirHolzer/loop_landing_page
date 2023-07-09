from selenium.webdriver.common.by import By

class TestLocators:


    LINK_TARIF_IN_HEADER = By.XPATH, ".//a[@href='/pricing/']"
    LINK_SUPPORT_IN_HEADER = By.XPATH, ".//a[@href='/support/']"
    LINK_DOWNLOAD_IN_HEADER = By.XPATH,  ".//a[@href='/download/']"

    HEADING_ON_SUPPORT_PAGE = By.XPATH,".//h2[text()='Написать нам']"
    HEADING_ON_DOWNLOAD_PAGE = By.XPATH, ".//h2[text() = 'Загрузить Loop для ']"
    DOWNLOAD_FOR_ANDROID_ON_DOWNLOAD_PAGE = By.XPATH,  ".//button[text() = 'Скачать для Android']"

    HEADING_ON_TARIF_PAGE = By.XPATH, ".//h2[@class='py-8 text-center leading-tight']"

    EMAIL_INPUT_REGISTRATION = By.XPATH, ".//fieldset[2]//input"
    PASSWORD_INPUT_REGISTRATION = By.NAME, "Пароль"
    REGISTRATION_BUTTON = By.TAG_NAME, "button"
    LOGIN_BUTTON_REGISTRATION = By.XPATH, ".//a[text()='Войти']"
    PASSWORD_INPUT_ERROR_REGISTRATION = By.XPATH, ".//p[text()='Некорректный пароль']"
