from deck import Deck
from card import Card
import random

def test_deck_len():
    new_deck = Deck()
    assert (len(new_deck.deck)) == 52


def test_new_deck_can_draw_card():
    """Tests that you did in fact draw a card and it was
    subtracted from the deck"""
    deck = Deck()
    card = deck.draw()
    assert card is not None
    assert len(deck) == 51


def test_deck_can_be_shuffled():
    deck = Deck()
    deck.shuffle_deck()
    assert deck != Deck()
