import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture()
def open_browser():
    browser.config.window_width = 100
    browser.config.window_height = 100
    browser.open('https://google.com')


@pytest.fixture()
def search_selene():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
