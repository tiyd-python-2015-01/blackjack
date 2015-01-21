from Deck import *
from Card import *

newdeck = Deck()


def test_get_length():
    assert newdeck.get_length() == 52


def test_init():
    assert newdeck.get_length() == 52
    assert isinstance(newdeck.deck[0], Card)


def test_deck_shuffle():
    assert newdeck.deck_shuffle() != newdeck


def test_deck_deal():
    assert type(newdeck.deal()) == Card
    assert newdeck.get_length() == 51
