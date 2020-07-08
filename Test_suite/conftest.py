
import pytest
import allure
from selenium import webdriver
from Test_suite.DB.client import DBClient
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
def db_client():
    db_client = DBClient()
    yield db_client
    db_client.close()


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
def setup_product_page(db_client, admin_product_page):
    data_1 = {'language_id': '1',
              'name': 'Vouse+21',
              'tag': 'Per',
              'meta_title': 'Per',
              'meta_description': 'Perr',
              'meta_keyword': 'perr'}
    data_2 = { "model": "Mouse+21",
                "sku": "Tr",
                "upc": "TRT",
                "ean": "wer",
                "jan": "wer",
                "isbn": "wer",
                "mpn": "wer",
                "location": "wer",
                "quantity": 1,
                "stock_status_id": 6,
                "manufacturer_id": 0,
                "tax_class_id": 0,
                "date_added": "2020-07-04 14:44:24",
                "date_modified": "2020-07-04 14:44:24"}
    if len(admin_product_page.check_product_in_db(product_name='Vouse+21')) == 0:
        admin_product_page.add_product_in_db(data=data_1)
        admin_product_page.add_product_in_db(table_name='oc_product', data=data_2)
        db_client.commit()


@allure.title('Предустановки для теста')
@pytest.fixture()
def admin_categories_page(remote):
    page = AdminCategoriesPage(remote)
    page.open()
    page.login_admin()
    page.go_to_categories()
    return page

