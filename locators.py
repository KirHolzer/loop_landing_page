from selenium.webdriver.common.by import By

class TestLocators:


    LINK_TARIF_IN_HEADER = By.XPATH, ".//header//a[@href='/pricing/']"
    LINK_SUPPORT_IN_HEADER = By.XPATH, ".//header//a[@href='/support/']"
    LINK_DOWNLOAD_IN_HEADER = By.XPATH,  ".//header//a[@href='/download/']"
    BUTTON_CREATE_TEAM_IN_HEADER = By.XPATH, ".//header//button[text() = 'Создать команду']"
    LOGO_LOOP_HEADER = By.XPATH, ".//header//img[@alt = 'logo']"
    HEADING_ON_MAIN_PAGE = By.XPATH, ".//h1[text()='Единый мессенджер для вашей ']"
    HEADING_ON_SUPPORT_PAGE = By.XPATH,".//h2[text()='Написать нам']"
    HEADING_ON_DOWNLOAD_PAGE = By.XPATH, ".//h2[text() = 'Загрузить Loop для ']"
    HEADING_ON_SIGN_UP_PAGE = By.XPATH, ".//h2[text() = 'Создать команду в Loop']"
    HEADING_ON_CONTACT_SALES = By.XPATH, ".//h2[text() = 'Оставить заявку']"
    DOWNLOAD_FOR_ANDROID_ON_DOWNLOAD_PAGE = By.XPATH,  ".//button[text() = 'Скачать для Android']"

    HEADING_ON_TARIF_PAGE = By.XPATH, ".//h2[@class='py-8 text-center leading-tight']"

    LINK_SIGN_UP_IN_FOOTER = By.XPATH, ".//footer//a[@href='/sign-up/']"
    LINK_DOWNLOAD_IN_FOOTER = By.XPATH, ".//footer//a[@href='/download/']"
    LINK_TARIF_IN_FOOTER = By.XPATH, ".//footer//a[@href='/pricing/']"
    LINK_CONTACT_SALES_IN_FOOTER = By.XPATH, ".//footer//a[@href='/contact-sales/']"
    LINK_SUPPORT_IN_FOOTER = By.XPATH, ".//footer//a[@href='/support/']"
    lINK_LOOP_CHAT_SUPPORT_TELEG_IN_FOOTER = By.XPATH, ".//footer//a[@href='https://t.me/loop_chat_support']"
    LINK_DOCS_FOR_USERS_IN_FOOTER = By.XPATH, ".//footer//a[@href = 'https://docs.loop.ru/']"
    LINK_DOCS_FOR_DEVELOPERS_IN_FOOTER = By.XPATH, ".//footer//a[@href = 'https://developers.loop.ru/']"
    LINK_DOCS_FOR_PRIVACY_POLICY_IN_FOOTER = By.XPATH, ".//footer//a[text() = 'Политика конфиденциальности']"

    DOCS_ELEMENT_FOR_USERS = By.XPATH, ".//h1[text() = 'Добро пожаловать']"
    DOCS_ELEMENT_FOR_DEVELOPERS = By.XPATH, ".//h1[text() = 'Добро пожаловать в документацию Loop для разработчиков']"
    DOCS_ELEMENT_FOR_PRIVACY_POLICY = By.XPATH, ".//strong[0]"
    # ".//a[text() = 'Руководство']"

    LOCATOR_ON_TELEGRAM_PAGE = By.XPATH, ".//a[@class = 'tgme_head_brand']"



    EMAIL_INPUT_REGISTRATION = By.XPATH, ".//fieldset[2]//input"
    PASSWORD_INPUT_REGISTRATION = By.NAME, "Пароль"
    REGISTRATION_BUTTON = By.TAG_NAME, "button"
    LOGIN_BUTTON_REGISTRATION = By.XPATH, ".//a[text()='Войти']"
    PASSWORD_INPUT_ERROR_REGISTRATION = By.XPATH, ".//p[text()='Некорректный пароль']"
