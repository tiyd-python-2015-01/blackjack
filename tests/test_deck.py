from deck import Deck
from card import Card


def test_new_deck_has_52_cards():
    assert len(Deck()) == 52


def test_new_deck_can_draw_card():
    deck = Deck()
    card = deck.draw()

    assert len(deck) == 51
    assert card is not None


def test_deck_can_be_shuffled():
    deck = Deck()
    deck.shuffle()

    assert deck != Deck()
