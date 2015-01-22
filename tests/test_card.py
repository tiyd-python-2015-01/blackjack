from card import Card
from deck import Deck


def test_Card():

    new_card = Card("King", "Spade")
    assert new_card.number == "King"
    assert new_card.suit == "Spade"



def test_deck():

    new_deck = Deck()
    assert new_deck.get_length() == 52
    new_deck.get_card()
    assert new_deck.get_length() == 51

    assert isinstance(new_deck.get_card(), Card)
    assert isinstance(new_deck.deck[1], Card)
