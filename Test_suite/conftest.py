import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions, FirefoxProfile

from Test_suite.pages.admin_categories_page import AdminCategoriesPage
from Test_suite.pages.admin_product_page import AdminProductPage

BROWSERSTACK_URL = 'https://bsuser70674:eW8i4mzi6j2ykdVUjjtB@hub-cloud.browserstack.com/wd/hub'

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='firefox',
        help='This is browser for testing',
        choices=["chrome", "firefox", "opera", "yandex"]
    )
    parser.addoption('--executor', action='store', default='192.168.0.107')


# @pytest.fixture()
# def firefox(request):
#     profile = FirefoxProfile()
#     profile.accept_untrusted_certs = True
#     wd = webdriver.Firefox(firefox_profile=profile)
#     request.addfinalizer(wd.quit())
#     return wd
#
#
# @pytest.fixture()
# def chrome(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit())
#     return wd
#
#
# @pytest.fixture
# def browser_opt(request):
#     return request.config.getoption('--browser')
#
#
# @pytest.fixture()
# def remote(request):
#     browser = request.config.getoption('--browser')
#     executor = request.config.getoption('--executor')
#     options = ChromeOptions()
#     if browser == 'chrome':
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--headless')
#         wd = webdriver.Remote(options=options, command_executor=f'http://{executor}:4444/wd/hub',
#                               desired_capabilities={'browserName': browser})
#     elif browser == 'firefox':
#         options = FirefoxOptions()
#         options.add_argument('--kiosk')
#         wd = webdriver.Remote(options=options,
#                               command_executor=f'http://{executor}:4444/wd/hub',
#                               desired_capabilities={'browserName': browser})
#     elif browser == 'IE':
#         options = IeOptions()
#         capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
#         capabilities['acceptSslCerts'] = True
#         capabilities['browserName'] = browser
#         wd = webdriver.Remote(options=options, command_executor=f'http://{executor}:4444/wd/hub',
#                               desired_capabilities=capabilities)
#     wd.maximize_window()
#     request.addfinalizer(wd.quit)
#     return wd

desired_cap = {
    'os' : 'Windows',
    'os_version' : '10',
    'browser' : 'Chrome',
    'browser_version' : '80',
    'name' : "bsuser70674's First Test"}

@pytest.fixture()
def remote():
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        desired_capabilities=desired_cap)
    yield driver
    driver.quit()

@pytest.fixture()
def admin_product_page(remote):
    page = AdminProductPage(remote)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    return page


@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@pytest.fixture()
def admin_categories_page(remote):
    page = AdminCategoriesPage(remote)
    page.open()
    page.login_admin()
    page.go_to_categories()
    return page






