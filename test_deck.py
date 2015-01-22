from deck import Deck
from card import Card


def test_create_deck():
    deck1 = Deck()
    assert len(deck1.cards) == 52
    assert isinstance(deck1.cards[0], Card)
