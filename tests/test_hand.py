from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand
from player import Player


def test_hand_receives_cards():
    """Will test that the hand receives a card from the shoe"""
    deck1 = Shoe()
    hand1 = Hand()
    hand1.add_card(deck1.deal_card())
    assert len(hand1.hand) == 1


def test_card_value():
    """Will test the ability of a hand to assess a card's value"""
    shoe = Shoe()
    test_hand = Hand()
    test_card = Card("J", "Hearts")
    test_hand.add_card(test_card)
    assert test_hand.get_hand_value() == 10


def test_hand_value():
    """Test the ability of a hand to calculate its own value"""
    shoe = Shoe()
    card1 = Card("J", "Hearts")
    card2 = Card("6", "Clubs")
    test_hand = Hand()
    test_hand.add_card(card2)
    test_hand.add_card(card1)
    print(test_hand)
    assert test_hand.get_hand_value() == 16
