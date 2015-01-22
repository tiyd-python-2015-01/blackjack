from blackjack.card import Card, ranks, suits
from blackjack.deck import Deck

def test_new_deck_has_52_cards():
    assert len(Deck()) == 52

def test_new_deck_can_draw_card():
    deck = Deck()
    card = deck.deal_cards()

    assert card is not None
    assert len(deck) == 51

def test_deck_can_be_shuffled():
    shuffled_deck = Deck()
    straight_deck = Deck()
    shuffled_deck.shuffle_deck()

    assert straight_deck != shuffled_deck
