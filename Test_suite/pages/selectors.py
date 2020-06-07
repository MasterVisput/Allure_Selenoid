from selenium.webdriver.common.by import By


class CatalogPageSelectors:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    BASKET_BUTTON = (By.XPATH, '//*[@id="cart"]/button')
    GRID_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    LIST_BUTTON = (By.XPATH, '//*[@id="list-view"]')
    LINK_PRODUCT_COMPARE = (By.CSS_SELECTOR, '#compare-total')


class ProductCardSelectors():
    BUTTON_ADD_TO_WISH_LIST = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    QTY_FIELD = (By.CSS_SELECTOR, '#input-quantity')
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, '#button-cart.btn-lg')
    BUTTON_COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    REVIEWS_LINK = (By.CSS_SELECTOR, '[href="#tab-review"]')


class LoginPageSelectors:
    BUTTON_CONTINUE = (By.XPATH, '//a[text()="Continue"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[value="Login"]')
    E_MAIL_FIELD = (By.CSS_SELECTOR, '[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.form-group a')


class LoginAdminPageSelector:
    USERNAME_FIELD = (By.CSS_SELECTOR, '[name="username"]')
    PASSWOD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    FORGOTTEN_PASSWORD = (By.XPATH, '//a[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    OPENCART_LINK = (By.XPATH, '//a[text()="OpenCart"]')


class DashboardPageSelectors:
    LOGOUT_LINK = (By.CSS_SELECTOR, '.hidden-xs')
    CATALOG_LINK = (By.CSS_SELECTOR, '[href="#collapse1"]')
    PRODUCT_LINK = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2)')
    CATEGORIES_LINK = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(1) > a')
    PRODUCT_TAB = (By.CSS_SELECTOR, 'tbody tr')
    CATEGORIES_TAB = (By.CSS_SELECTOR, '.table-responsive tr')
    ADD_NEW = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    DELETE = (By.CSS_SELECTOR, '[data-original-title="Delete"]')
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter[type="button"]')
    DASHBOARD_LINK = (By.CSS_SELECTOR, '#menu-dashboard')
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success')
    EDIT_IN_P_TAB = (By.CSS_SELECTOR, 'tr td:nth-child(8) [data-toggle="tooltip"]')
    CHECKBOX_IN_P_TAB = (By.CSS_SELECTOR, 'tr td:nth-child(1)')
    NAME_P_IN_P_TAB = (By.CSS_SELECTOR, 'tr td:nth-child(3)')


class AddNewProductCartSelectors:
    SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    EDIT_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Edit"]')

    GENERAL_TAB = (By.CSS_SELECTOR, '[href="#tab-general"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TAG = (By.CSS_SELECTOR, '#input-meta-title1')

    DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
    MODEL = (By.CSS_SELECTOR, '[name="model"]')
    IMAGE_TAB = (By.CSS_SELECTOR, '[href="#tab-image"]')
    IMAGE = (By.CSS_SELECTOR, 'a#thumb-image')
    BUTTON_IMAGE = (By.CSS_SELECTOR, 'button-image')
    INPUT_IMAGE = (By.CSS_SELECTOR, '#input-image')

class CategoriesPageSelectors:
    REBUILD_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Rebuild"]')

class MozillaPageSelectors:
    INPUT_ELEMENT = (By.CSS_SELECTOR, '[name="myFile"]')
    IFRAME = (By.CSS_SELECTOR, '#frame_file-example')

