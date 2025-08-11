import pytest
from selene import browser, have


@pytest.fixture(scope="function")
def setup_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.config.timeout = 6  # увеличил таймаут ожидания до 6 сек
    browser.open('https://ya.ru')
    yield
    browser.quit()

def test_input_value(setup_browser):
    browser.element('#text').type('погода Санкт-Петербург').press_enter()
    browser.element('input[name="text"]').should(have.value('погода Санкт-Петербург'))

def test_broke_search(setup_browser):
    browser.element('#text').type('"Жаброкогтельный флюкскварц 38QZ-LR-α"').press_enter()
    browser.element('.RequestMeta-Message').should(have.text('Точного совпадения не нашлось. Показаны результаты по запросу без кавычек.')
    )