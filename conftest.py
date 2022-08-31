import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 1000
    browser.open('https://google.com')


@pytest.fixture()
def search_selene():
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
