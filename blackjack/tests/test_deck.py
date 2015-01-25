from deck import *
from card import *

newdeck = Deck()


def test_get_length():
    assert newdeck.get_length() == 52


def test_init():
    assert newdeck.get_length() == 52
    assert isinstance(newdeck.deck[0], Card)
    assert isinstance(newdeck, Deck)


def test_deck_shuffle():
    olddeck = newdeck
    newdeck.shuffle()
    assert newdeck.get_length() == 52


def test_deck_deal():
    assert type(newdeck.deal()) == Card
    assert newdeck.get_length() == 51
