from card import Card
from deck import Deck


def test_deck_generate():
    assert Deck()


def test_deck_length():
    assert len(Deck()) == 52
