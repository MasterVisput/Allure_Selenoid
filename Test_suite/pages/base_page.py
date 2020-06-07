from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Test_suite.pages.selectors import LoginAdminPageSelector, DashboardPageSelectors


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'http://localhost/admin'

    def find_element(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable(locator))

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(
            EC.visibility_of_all_elements_located(locator))

    def find_dom_element(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located(locator))

    def is_element_present(self, locator, time=5):
        try:
            wait = WebDriverWait(self.browser, time).until(
                EC.presence_of_all_elements_located(locator))
            return True
        except TimeoutException:
            return False

    def open(self):
        return self.browser.get(self.base_url)

    def login_admin(self):
        username_field = self.find_element(LoginAdminPageSelector.USERNAME_FIELD)
        username_field.send_keys('user')
        password_field = self.find_element(LoginAdminPageSelector.PASSWOD_FIELD)
        password_field.send_keys('bitnami1')
        login_button = self.find_element(LoginAdminPageSelector.LOGIN_BUTTON)
        login_button.click()
        try:
            wait = WebDriverWait(self.browser, 5).until(EC.title_contains('Dashboard'))
            return self.browser.title
        except TimeoutException:
            return 'TimeoutException'

    def log_out(self):
        logout_link = self.find_element(DashboardPageSelectors.LOGOUT_LINK)
        logout_link.click()
        try:
            wait = WebDriverWait(self.browser, 5).until(EC.title_contains('Administration'))
            return self.browser.title
        except TimeoutException:
            return 'TimeoutException'
