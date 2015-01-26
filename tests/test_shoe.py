from shoe import Shoe
from deck import Deck
from card import Card


def test_shoe_length():
    """Test shoe is six decks large"""

    shoe = Shoe()
    assert len(shoe) == 312


def test_get_card():
    """Test shoe can pull out a card"""

    shoe = Shoe()
    assert isinstance(shoe.get_card(), Card)
    shoe.get_card()
    assert len(shoe) == 310


def test_shoe_refill():
    """Test shoe refill fn, fills the shoe to 312 cards"""

    shoe = Shoe()
    shoe.get_card()
    assert len(shoe) == 311
    shoe.refill()
    assert len(shoe) == 312
