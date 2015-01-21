from deck import Deck
from card import Card

def test_deck_creation():
    new_deck = Deck()
    assert new_deck

def test_deck_length():
    new_deck = Deck()
    assert len(new_deck.cards) == 52

def test_shoe_creation():
    new_deck = Deck(2)
    assert len(new_deck.cards) == 104
    new_deck_2 = Deck(4)
    assert len(new_deck_2.cards) == 208

def test_shuffle_deck():
    suits = ["hearts", "spades", "clubs", "diamonds"]
    names = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "J", "Q", "K"]
    unshuffled_deck = [Card(name, suit) for suit in suits
                                        for name in names]
    new_deck = Deck()

    assert new_deck.cards != unshuffled_deck

def test_deal_cards():
    new_deck = Deck()
    assert new_deck.deal_card()
