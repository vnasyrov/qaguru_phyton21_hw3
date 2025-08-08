import pytest
from selene import browser, have


@pytest.fixture
def open_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.open('https://ya.ru')
    yield
    browser.quit()


def test_input_value(open_browser):
    browser.element('[id="text"]').type('погода Санкт-Петербург').press_enter()
    browser.element('input[name="text"]').should(have.value('погода Санкт-Петербург'))

def test_broke_search(open_browser):
    browser.element('[id="text"]').type('"Жаброкогтельный флюкскварц 38QZ-LR-α"').press_enter()
    browser.element('[class="RequestMeta-Message"]').should(have.text('Точного совпадения не нашлось. Показаны результаты по запросу без кавычек.'))