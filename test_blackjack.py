import deck as dk
import card
import shoe
from hand import Hand, get_hand_value

def test_deck_creation():
    test_deck = dk.Deck()
    assert len(test_deck.deck) == 52

# def test_deck_is_made_of_cards():
#     test_deck = dk.Deck
#     for _card in test_deck.deck:
#         assert _card == (Card.rank, Card.suit)

def test_card_creation():
    test_card = card.Card
    assert str(card.Card("Jack", "Diamonds")) == "Jack of Diamonds"
#
# def test_shuffle():
#     test_deck = shoe.Shoe()
#     assert len(test_deck.shuffle_shoe) == 52

def test_hand_value():
    test_hand = Hand(card.Card("K", 9)
    assert get_hand_value(test_hand) == 19
