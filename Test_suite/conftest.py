import pytest
from selenium import webdriver

from Test_suite.pages.admin_categories_page import AdminCategoriesPage
from Test_suite.pages.admin_product_page import AdminProductPage


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='opera',
        help='This is browser for testing',
        choices=["chrome", "firefox", "opera", "yandex"]
    )
    parser.addoption('--selenoid', action='store', default='localhost')


@pytest.fixture()
def remote(request):
    browser = request.config.getoption('--browser')
    selenoid = request.config.getoption('--selenoid')
    executor_url = f'http://{selenoid}:4444/wd/hub'
    caps = {'browserName': browser,
            'enableVnc': True,
            'version': '66.0',
            # 'enableVideo': True,
            'enableLog': True,
            'screenResolution': '1280x720',
            'name': request.node.name}
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@pytest.fixture()
def admin_product_page(remote):
    page = AdminProductPage(remote)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    return page


@pytest.fixture()
def admin_categories_page(remote):
    page = AdminCategoriesPage(remote)
    page.open()
    page.login_admin()
    page.go_to_categories()
    return page
