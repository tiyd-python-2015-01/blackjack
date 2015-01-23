from deck import Deck
from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand

def test_deck_creation():
    """Tests the ability of the deck to create a list of 52 cards"""
    test_deck = Deck()
    assert len(test_deck.deck) == 52


def test_card_creation():
    """Will test the __str__ output of the Card class"""
    test_card = Card("Jack", "Diamonds")
    assert str(test_card) == "Jack of Diamonds"


def test_deck_creation_in_shoe_class():
    """Tests the ability of the shoe to create deck"""
    test_deck = Shoe()
    assert len(test_deck.deck) == 52


def test_shuffle():
    """test the ability of the shoe to shuffle a deck"""
    deck1 = Shoe()
    deck2 = Shoe()
    deck1.shuffle_shoe()
    deck2.shuffle_shoe()
    assert deck1.shuffle_shoe() != deck2.shuffle_shoe()


# def test_hand_value():
#     """Will test the ability of a hand to assess its value"""
#     test_hand = Hand(card.Card("K", 9)
#     assert get_hand_value(test_hand) == 19
