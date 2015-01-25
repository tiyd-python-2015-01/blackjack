from blackjack.card import Card
from blackjack.deck import Deck


def test_deck():
    a_deck = Deck()
    assert len(a_deck.cards) == 52


def test_deck_draw():
    a_deck = Deck()
    a_deck.draw()
    assert len(a_deck.cards) == 51
