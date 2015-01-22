from blackjack.card import Card, ranks, suits
from blackjack.deck import Deck

def test_suit_and_rand_are_set():
    new_card = Card("Q", "Hearts")
    assert new_card.rank == "Q"
    assert new_card.suit == "Hearts"

def test_identical_cards_are_equal():
    queen1 = Card("Q", "Hearts")
    queen2 = Card("Q", "Hearts")

    assert queen1 == queen2

#def test_card_representation_is_readable():
#    queen = Card
#    assert repr(queen) == "Card('Q')"
