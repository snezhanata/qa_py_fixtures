from selene.support.shared import browser
from selene import have


def test_search_selene_positive(search_selene):
    assert browser.element('[id="search"]').should(have.text('yashaka/selene:'))
    print("Positive")


def test_search_selene_negative(search_selene):
    assert browser.element('[id="search"]').should(have.no.text('harry potter'))
    print("Negative")
