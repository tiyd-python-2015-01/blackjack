from card import Card
from card import card_numbers
from card import card_suits

def test_card_lists():
    """Testing import of rank and suit lists..."""
    assert "King" in card_numbers
    assert "Spades" in card_suits
    assert len(card_numbers) == 13
    assert len(card_suits) == 4

def test_Card():
    "Testing making a new card"

    new_card = Card("King", "Spades")
    assert new_card.number == "King"
    assert new_card.suit == "Spades"

def test_str_output():
    """Testing the str output of cards"""
    new_card = Card("2", "Diamonds")
    assert str(new_card) == "2 of Diamonds"
    new_card = Card("5", "Clubs")
    assert str(new_card) != "2 of Clubs"
