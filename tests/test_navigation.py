from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from my_data import TestUrls
#from my_data import TestConstructorNavigationText

class TestNavigation:

    def test_go_to_tarif_from_main_header(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_TARIF_IN_HEADER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_TARIF_PAGE))
        assert browser.current_url == TestUrls.tariff_page_url

    def test_go_to_support_from_main_header(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_SUPPORT_IN_HEADER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_SUPPORT_PAGE))
        assert browser.current_url == TestUrls.support_page_url

    def test_go_to_download_from_main_header(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_DOWNLOAD_IN_HEADER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_DOWNLOAD_PAGE))
        assert browser.current_url == TestUrls.download_apps_page_url

    def test_go_to_sign_up_from_main_header(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.BUTTON_CREATE_TEAM_IN_HEADER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_SIGN_UP_PAGE))
        assert browser.current_url == TestUrls.sign_up_page_url

    def test_go_to_main_from_sign_up_header(self, browser):
        browser.get(TestUrls.sign_up_page_url)
        browser.find_element(*TestLocators.LOGO_LOOP_HEADER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_MAIN_PAGE))
        assert browser.current_url == TestUrls.main_url

    def test_go_to_sign_up_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_SIGN_UP_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_SIGN_UP_PAGE))
        assert browser.current_url == TestUrls.sign_up_page_url

    def test_go_to_download_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_DOWNLOAD_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_DOWNLOAD_PAGE))
        assert browser.current_url == TestUrls.download_apps_page_url

    def test_go_to_tarif_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_TARIF_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_TARIF_PAGE))
        assert browser.current_url == TestUrls.tariff_page_url

    def test_go_to_contact_sales_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_CONTACT_SALES_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_CONTACT_SALES))
        assert browser.current_url == TestUrls.contact_sales_page_url

    def test_go_to_support_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_SUPPORT_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_ON_SUPPORT_PAGE))
        assert browser.current_url == TestUrls.support_page_url

    def test_go_to_loop_chat_support_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.lINK_LOOP_CHAT_SUPPORT_TELEG_IN_FOOTER).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOCATOR_ON_TELEGRAM_PAGE))
        assert browser.current_url == TestUrls.telegram_chat_support_page_url

    def test_go_to_docs_for_users_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_DOCS_FOR_USERS_IN_FOOTER).click()
        browser.switch_to.window(browser.window_handles[-1])
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.DOCS_ELEMENT_FOR_USERS))
        assert browser.current_url == TestUrls.docs_for_users_url

    def test_go_to_docs_for_developers_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_DOCS_FOR_DEVELOPERS_IN_FOOTER).click()
        browser.switch_to.window(browser.window_handles[-1])
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.DOCS_ELEMENT_FOR_DEVELOPERS))
        assert browser.current_url == TestUrls.docs_for_developers_url

    def test_go_to_docs_privocy_policy_from_main_footer(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LINK_DOCS_FOR_PRIVACY_POLICY_IN_FOOTER).click()
        browser.switch_to.window(browser.window_handles[-1])
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.DOCS_ELEMENT_FOR_PRIVACY_POLICY))
        assert browser.current_url == TestUrls.docs_privacy_policy_url


