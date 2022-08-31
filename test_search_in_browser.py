from selene.support.shared import browser
from selene import have


def test_search_selene_positive(search_selene):
    browser.element('[id="search"]').should(have.text('yashaka/selene:'))
    # Использование assert и should(have) избыточно, достаточно применить что-то одно
    # .should - имеет встроенные ожидания
    # а все что мы тестируем в вебе - динамическое, и ожидание нам нужно всегда
    # Поэтому для всех асертов по веб элементам - используем .should

    print("Positive")


def test_search_selene_negative(search_selene):
    browser.element('[id="search"]').should(have.no.text('harry potter'))
    print("Negative")
