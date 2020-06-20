import allure
from selenium.webdriver.support.events import AbstractEventListener


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        with allure.step(f'Выполняю переход на сайт {url}'):
            pass

    def after_navigate_to(self, url, driver):
        with allure.step(f'Выполнен переход на сайт {url}'):
            pass

    def before_navigate_back(self, driver):
        with allure.step('Выполняется возврат'):
            pass

    def after_navigate_back(self, driver):
        with allure.step('Выполнен возврат'):
            pass

    def before_find(self, by, value, driver):
        with allure.step(f'Выполняется поиск {value} по {by}'):
            pass

    def after_find(self, by, value, driver):
        with allure.step(f'Найден элемент {value} по {by}'):
            pass

    def before_click(self, element, driver):
        with allure.step(f'Выполняется клик по {element}'):
            pass

    def after_click(self, element, driver):
        with allure.step(f'Выполнен клик по {element}'):
            pass

    def before_execute_script(self, script, driver):
        with allure.step(f'Применяется скрипт JS:  {script}'):
            pass

    def after_execute_script(self, script, driver):
        with allure.step(f'Применён JS скрипт {script}'):
            pass

    def before_quit(self, driver):
        with allure.step('Выполняю выход из браузера'):
            pass
        browser_logs = driver.get_log('browser')
        logs = []
        for el in browser_logs:
            logs.append([])
            if el['level'] == 'SEVERE':
                logs[-1].append(el)
        allure.attach(body=str(logs),
                      name='browser_err_logs',
                      attachment_type=allure.attachment_type.TEXT)

    def after_quit(self, driver):
        with allure.step('Выполнен выход из браузера'):
            pass

    def on_exception(self, exception, driver):
        allure.attach(body=driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
