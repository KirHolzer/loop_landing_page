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