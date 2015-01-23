from deck import Deck
from card import Card


def test_deck_init():
    a_deck = Deck()
    assert isinstance(a_deck.cards[0], Card)


def test_deck_shuffle():
    a_deck = Deck()
    a_second_deck = Deck()
    assert a_deck == a_second_deck
    a_deck.shuffle()
    assert not a_deck == a_second_deck


def test_deck_draw():
    a_deck = Deck()
    a_deck.draw()
    assert len(a_deck) == 51

    
