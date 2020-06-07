from Test_suite.pages.selectors import DashboardPageSelectors


class TestProductsPage:
    def test_add_new_pruduct(self, admin_product_page):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продкт не добавлен'

    def test_delete_product_by_name(self, admin_product_page, setup_product_page):
        admin_product_page.delete_product_from_tab(p_name='Mouse')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не удалён'

    def test_edit_product_by_name(self, admin_product_page, setup_product_page):
        admin_product_page.edit_product_from_tab(p_name='Mouse', new_p_name='Mouse+21')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не отредактирован'

    def test_product_filter(self, admin_product_page, setup_product_page):
        assert admin_product_page.is_product_in_tab(p_name='Mouse'), 'Продукта нет в таблице'


class TestCategoriesPage:
    def test_rebuild_tab(self, admin_categories_page):
        admin_categories_page.rebuild_page()
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)

    def test_categories_tab_is_present(self, admin_categories_page):
        assert admin_categories_page.is_element_present(DashboardPageSelectors.CATEGORIES_TAB)

    def test_add_category(self, admin_categories_page):
        admin_categories_page.add_new_categoriy(c_name='Lamp', m_tag='Lamps')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)

    def test_edit_category_by_name(self, admin_categories_page):
        admin_categories_page.edit_category(c_name='Lamp', new_c_name='Lamp mini')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)
