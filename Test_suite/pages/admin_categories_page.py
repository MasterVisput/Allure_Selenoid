from Test_suite.pages.base_page import BasePage
from Test_suite.pages.selectors import CategoriesPageSelectors, DashboardPageSelectors, AddNewProductCartSelectors


class AdminCategoriesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def rebuild_page(self):
        rebuild_button = self.find_element(CategoriesPageSelectors.REBUILD_BUTTON)
        rebuild_button.click()
        self.browser.execute_script("console.error('Here is the ERROR message!')")

    def go_to_categories(self):
        catalog_link = self.find_element(DashboardPageSelectors.CATALOG_LINK)
        catalog_link.click()
        categories_link = self.find_element(DashboardPageSelectors.CATEGORIES_LINK)
        categories_link.click()

    def add_new_categoriy(self, c_name='Lamp', m_tag='Lamps'):
        add_new_button = self.find_element(DashboardPageSelectors.ADD_NEW)
        add_new_button.click()
        general_tab = self.find_element(AddNewProductCartSelectors.GENERAL_TAB)
        general_tab.click()
        category_name = self.find_element(AddNewProductCartSelectors.PRODUCT_NAME)
        category_name.send_keys(c_name)
        meta_tag = self.find_element(AddNewProductCartSelectors.META_TAG)
        meta_tag.send_keys(m_tag)
        save_button = self.find_element(AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()

    def edit_category(self, c_name='Lamp', new_c_name='Lamp mini'):
        edit_button = self.get_edit_button_by_category_name(c_name)
        edit_button.click()
        product_name_field = self.find_element(AddNewProductCartSelectors.PRODUCT_NAME)
        product_name_field.clear()
        product_name_field.send_keys(new_c_name)
        save_button = self.find_element(AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()

    def get_edit_button_by_category_name(self, c_name='Lamp'):
        categories_tab = self.find_elements(DashboardPageSelectors.CATEGORIES_TAB)
        for el in categories_tab:
            name = el.find_element_by_css_selector('tr td:nth-child(2)')
            if name.text == c_name:
                edit_button = el.find_element_by_css_selector('[data-original-title="Edit"]')
                return edit_button


