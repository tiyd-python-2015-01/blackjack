from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand
from player import Player

def test_card_creation():
    """Will test the __str__ output of the Card class"""
    test_card = Card("Jack", "Diamonds")
    assert str(test_card) == "Jack of Diamonds"
