from deck import Deck
from card import Card

def test_deck():
    """Test creating a deck makes the correct amount of cards and
    that the __len__ fn will work."""

    new_deck = Deck()
    assert len(new_deck) == 52
    new_deck.get_card()
    assert len(new_deck) == 51
    assert isinstance(new_deck.get_card(), Card)
    assert isinstance(new_deck.deck[1], Card)

def test_getting_a_hand():
    """Test making a hand of two cards, getting another card/resulting hand and
    deck lengths."""

    new_deck = Deck()
    a_hand = []

    for _ in range(0,2):
        a_hand.append(new_deck.get_card())

    assert len(a_hand) == 2
    assert len(new_deck) == 50

    a_hand.append(new_deck.get_card())

    assert len(a_hand) == 3

    assert len(new_deck) ==49
