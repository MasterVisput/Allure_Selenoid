import allure

from Test_suite.pages.selectors import DashboardPageSelectors


class TestProductsPage:
    @allure.feature('Страница редактирования продуктов')
    @allure.story('Работа с данными')
    @allure.title('Добавить новый продукт')
    def test_add_new_pruduct(self, admin_product_page):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продкт не добавлен'
        assert admin_product_page.check_product_in_db(product_name='Mouse') != 0

    @allure.feature('Страница редактирования продуктов')
    @allure.story('Работа с данными')
    @allure.title('Удалить продукт')
    def test_delete_product_by_name(self, admin_product_page, setup_product_page):
        admin_product_page.delete_product_from_tab(p_name='Vouse+21')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не удалён'
        assert admin_product_page.check_product_in_db(product_name='Vouse+21') == 0

    @allure.feature('Страница редактирования продуктов')
    @allure.story('Работа с данными')
    @allure.title('Отредактировать продукт')
    def test_edit_product_by_name(self, admin_product_page, setup_product_page):
        admin_product_page.edit_product_from_tab(p_name='Vouse+21', new_p_name='Mouse+21')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не отредактирован'
        assert admin_product_page.check_product_in_db(product_name='Vouse+21') != 0

    @allure.feature('Страница редактирования продуктов')
    @allure.story('Оотображение информации')
    @allure.title('Проверить поиск продукта')
    def test_product_filter(self, admin_product_page, setup_product_page):
        assert admin_product_page.is_product_in_tab(p_name='Mouse'), 'Продукта нет в таблице'


class TestCategoriesPage:
    @allure.feature('Страница редактирования категорий')
    @allure.story('Оотображение информации')
    @allure.title('Проверить кнопку Rebuild')
    def test_rebuild_tab(self, admin_categories_page):
        admin_categories_page.rebuild_page()
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)

    @allure.feature('Страница редактирования категорий')
    @allure.story('Оотображение информации')
    @allure.title('Проверка отображения категорий')
    def test_categories_tab_is_present(self, admin_categories_page):
        assert admin_categories_page.is_element_present(DashboardPageSelectors.CATEGORIES_TAB)

    @allure.feature('Страница редактирования категорий')
    @allure.story('Работа с данными')
    @allure.title('Добавление категории')
    def test_add_category(self, admin_categories_page):
        admin_categories_page.add_new_categoriy(c_name='Lamp', m_tag='Lamps')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)

    @allure.feature('Страница редактирования категорий')
    @allure.story('Работа с данными')
    @allure.title('Редактирование категории')
    def test_edit_category_by_name(self, admin_categories_page):
        admin_categories_page.edit_category(c_name='Lamp', new_c_name='Lamp mini')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)
