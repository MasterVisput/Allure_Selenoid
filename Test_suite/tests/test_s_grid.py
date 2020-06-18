import allure

class TestGrid():
    @allure.feature('feature1')
    @allure.story('story1')
    @allure.title('Тест яндекса')
    def test_yandex(self, remote):
        remote.get('https://yandex.ru/')
        title = remote.title
        assert title == 'Яндекс'

    @allure.feature('feature2')
    @allure.story('story2')
    @allure.title('Тест гугла')
    def test_google(self, remote):
        remote.get('https://www.google.ru/')
        title = remote.title
        assert title == 'Google'

    @allure.feature('feature1')
    @allure.story('story1')
    @allure.title('Тест хабра')
    def test_habr(self, remote):
        remote.get('https://habr.com/ru/')
        title = remote.title
        assert title == 'Лучшие публикации за сутки / Хабр'

    @allure.feature('feature2')
    @allure.story('story2')
    @allure.title('Тест ВК')
    def test_vk(self, remote):
        remote.get('https://vk.com/feed')
        title = remote.title
        assert title == 'VK'

    @allure.feature('feature1')
    @allure.story('story1')
    @allure.title('Тест погоды')
    def test_gmc(self, remote):
        remote.get('https://meteoinfo.ru/')
        title = remote.title
        assert title == 'Погода и подробный прогноз погоды от Гидрометцентра России'