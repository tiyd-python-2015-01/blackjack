from random import shuffle
from card import Card
from deck import Deck


def test_deck_length():
    new_deck = Deck()
    assert (len(new_deck.deck)) == 52

def test_draw_card():
    deck = Deck()
    card = deck.draw()

    assert card is not None
    assert len(deck) == 51

def test_deck_shuffle():
    new_deck = Deck()
    assert new_deck.shuffle_deck() != new_deck
