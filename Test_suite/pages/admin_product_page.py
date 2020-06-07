from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Test_suite.pages.base_page import BasePage
from Test_suite.pages.selectors import DashboardPageSelectors, AddNewProductCartSelectors


class AdminProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def go_to_product_tab(self):
        dashboard_link = self.find_element(DashboardPageSelectors.DASHBOARD_LINK)
        dashboard_link.click()
        catalog_link = self.find_element(DashboardPageSelectors.CATALOG_LINK)
        catalog_link.click()
        product_link = self.find_element(DashboardPageSelectors.PRODUCT_LINK)
        product_link.click()

    def return_product_tab(self):
        self.go_to_product_tab()
        try:
            return self.find_elements(DashboardPageSelectors.PRODUCT_TAB)
        except TimeoutException:
            return 'TimeoutException'

    def add_new_product(self, p_name='Mouse', m_tag='pereferi', model='M23-546S'):
        add_new_product_button = self.find_element(DashboardPageSelectors.ADD_NEW)
        add_new_product_button.click()
        product_name = self.find_element(AddNewProductCartSelectors.PRODUCT_NAME)
        product_name.send_keys(p_name)
        meta_tag = self.find_element(AddNewProductCartSelectors.META_TAG)
        meta_tag.send_keys(m_tag)
        self.find_element(AddNewProductCartSelectors.DATA_TAB).click()
        model_field = self.find_element(AddNewProductCartSelectors.MODEL)
        model_field.send_keys(model)
        save_button = self.find_element(AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()

    def is_product_in_tab(self, p_name='Mouse'):
        self.go_to_product_tab()
        product_name_field = self.find_element(DashboardPageSelectors.PRODUCT_NAME_FIELD)
        product_name_field.send_keys(p_name)
        filter_button = self.find_element(DashboardPageSelectors.FILTER_BUTTON)
        filter_button.click()
        products_tab = self.find_elements(DashboardPageSelectors.PRODUCT_TAB)
        try:
            for el in products_tab:
                name = el.find_element_by_css_selector('tr td:nth-child(3)')
                if name.text == p_name:
                    return True
        except NoSuchElementException:
            return False
        return False

    def get_element_from_tab_by_product_name(self, p_name='Mouse', selector=DashboardPageSelectors.EDIT_IN_P_TAB):
        products_tab = self.find_elements(DashboardPageSelectors.PRODUCT_TAB)
        for el in products_tab:
            name = el.find_element_by_css_selector(DashboardPageSelectors.NAME_P_IN_P_TAB[1])
            if name.text == p_name:
                return_element = el.find_element_by_css_selector(selector[1])
                return return_element

    def delete_product_from_tab(self, p_name='Mouse'):
        checkbox = self.get_element_from_tab_by_product_name(p_name=p_name,
                                                             selector=DashboardPageSelectors.CHECKBOX_IN_P_TAB)
        checkbox.click()
        delete_button = self.find_element(DashboardPageSelectors.DELETE)
        delete_button.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()

    def edit_product_from_tab(self, p_name='Mouse', new_p_name='Mouse+21'):
        edit_button = self.get_element_from_tab_by_product_name(p_name, selector=DashboardPageSelectors.EDIT_IN_P_TAB)
        edit_button.click()
        product_name_field = self.find_element(AddNewProductCartSelectors.PRODUCT_NAME)
        product_name_field.clear()
        product_name_field.send_keys(new_p_name)
        save_button = self.find_element(AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()

    def add_image_to_product_by_name(self, path, p_name):
        edit_button = self.get_element_from_tab_by_product_name(p_name=p_name,
                                                                selector=DashboardPageSelectors.EDIT_IN_P_TAB)
        edit_button.click()
        image_tab = self.find_element(AddNewProductCartSelectors.IMAGE_TAB)
        image_tab.click()
        js = "document.getElementById('input-image').style.display = 'inline'"
        self.browser.execute_script(js)
        input = self.browser.find_element_by_id('input-image')
        input.send_keys(path)
