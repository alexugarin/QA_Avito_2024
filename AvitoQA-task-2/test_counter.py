import os
import pytest
from playwright.sync_api import sync_playwright

# Фикстура для запуска браузера Chromium
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# Фикстура для создания контекста для того, чтобы не перезапускать браузер на каждый тест
@pytest.fixture(scope="module")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Инициализация списка тестов из файлов в директории mock
tests = [os.path.splitext(file)[0] for file in os.listdir('mock/')]

# Тесты для проверки счетчиков на странице
@pytest.mark.parametrize('test', tests)
def test_counter(context, test):
    page = context.new_page() # Новая страница
    # Перенаправление запроса к API для проверки результатов тестов
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init",
               lambda route: route.fulfill(path="mock/{}.json".format(test)))
    # Переход на тестируемую страницу
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    # Сохраняем скриншот элемента обертки счетчиков
    counter = page.locator(".desktop-wrapper-OutiE")
    counter.screenshot(path="output/{}.png".format(test))
