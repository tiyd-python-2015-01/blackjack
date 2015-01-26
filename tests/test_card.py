from card import Card
from shoe import Clubs, Hearts, Spades


def test_create_card():
    card1 = Card(2, Spades)
    assert card1.rank == 2
    assert card1.suit == Spades


def test_cards_are_equal():
    card1 = Card(3, Hearts)
    card2 = Card(3, Hearts)
    assert card1 == card2


def test_card_can_print_itself():
    card = Card('Q', Clubs)
    assert repr(card) == 'Q' + Clubs
