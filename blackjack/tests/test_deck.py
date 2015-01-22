from deck import Deck
from card import Card

def test_deck_init():
    a_deck = Deck()
    assert isinstance(a_deck.cards[0], Card)
