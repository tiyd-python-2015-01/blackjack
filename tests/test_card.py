from blackjack.card import Card, ranks, suits
from blackjack.shoe import Shoe
from blackjack.hand import Hand
from blackjack.player import Player

def test_card_creation():
    """Will test the __str__ output of the Card class"""
    test_card = Card("Jack", "Diamonds")
    assert str(test_card) == "Jack of Diamonds"
