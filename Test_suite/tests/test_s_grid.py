class TestGrid():
    def test_yandex(self, remote):
        remote.get('https://yandex.ru/')
        title = remote.title
        assert title == 'Яндекс'

    def test_google(self, remote):
        remote.get('https://www.google.ru/')
        title = remote.title
        assert title == 'Google'

    def test_habr(self, remote):
        remote.get('https://habr.com/ru/')
        title = remote.title
        assert title == 'Лучшие публикации за сутки / Хабр'

    def test_vk(self, remote):
        remote.get('https://vk.com/feed')
        title = remote.title
        assert title == 'VK'

    def test_gmc(self, remote):
        remote.get('https://meteoinfo.ru/')
        title = remote.title
        assert title == 'Погода и подробный прогноз погоды от Гидрометцентра России'