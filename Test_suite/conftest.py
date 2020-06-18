# import pytest
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
#
# from Test_suite.pages.admin_categories_page import AdminCategoriesPage
# from Test_suite.pages.admin_product_page import AdminProductPage
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser',
#         action='store',
#         default='chrome',
#         help='This is browser for testing',
#         choices=["chrome", "firefox", "opera", "yandex"]
#     )
#     parser.addoption('--selenoid', action='store', default='localhost')
#
#
# @pytest.fixture()
# def remote(request):
#     browser = request.config.getoption('--browser')
#     selenoid = request.config.getoption('--selenoid')
#     executor_url = f'http://{selenoid}:4444/wd/hub'
#     caps = {'browserName': browser,
#             'enableVnc': True,
#             'version': '83.0',
#             'enableVideo': True,
#             'enableLog': True,
#             'screenResolution': '1280x720',
#             'name': request.node.name}
#     options = ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Remote(options=options, command_executor=executor_url, desired_capabilities=caps)
#     request.addfinalizer(driver.quit)
#     return driver
#
#
# @pytest.fixture()
# def setup_product_page(admin_product_page):
#     if not admin_product_page.is_product_in_tab(p_name='Mouse'):
#         admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')
#
#
# @pytest.fixture()
# def admin_product_page(remote):
#     page = AdminProductPage(remote)
#     page.open()
#     page.login_admin()
#     page.go_to_product_tab()
#     return page
#
#
# @pytest.fixture()
# def admin_categories_page(remote):
#     page = AdminCategoriesPage(remote)
#     page.open()
#     page.login_admin()
#     page.go_to_categories()
#     return page

import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from Test_suite.pages.admin_categories_page import AdminCategoriesPage
from Test_suite.pages.admin_product_page import AdminProductPage
from selenium.webdriver.support.events import EventFiringWebDriver
from Test_suite.pages.listener import MyListener


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='This is browser for testing'
    )


@pytest.fixture
def browser_opt(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def remote(browser_opt):
    if browser_opt == 'Chrome':
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        browser = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=caps), MyListener())
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        browser = webdriver.Firefox()
    elif browser_opt == 'IE':
        browser = webdriver.Ie()
    yield browser
    browser.quit()


@allure.title('Предустановки для теста')
@pytest.fixture()
def admin_product_page(remote):
    page = AdminProductPage(remote)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    return page


@allure.title('Проверка наличия нужного продукта')
@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@allure.title('Предустановки для теста')
@pytest.fixture()
def admin_categories_page(remote):
    page = AdminCategoriesPage(remote)
    page.open()
    page.login_admin()
    page.go_to_categories()
    return page

