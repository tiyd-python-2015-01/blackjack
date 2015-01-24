from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand
from player import Player

def test_card_creation():
    """Will test the __str__ output of the Card class"""
    test_card = Card("Jack", "Diamonds")
    assert str(test_card) == "Jack of Diamonds"


def test_deck_creation_in_shoe_class():
    """Tests the ability of the shoe to create deck"""
    test_deck = Shoe()
    assert len(test_deck.deck) == 52


def test_shuffle():
    """test the ability of the shoe to shuffle a deck"""
    deck1 = Shoe()
    deck2 = Shoe()
    deck1.shuffle_shoe()
    deck2.shuffle_shoe()
    assert deck1.shuffle_shoe() != deck2.shuffle_shoe()


def test_for_dealing_card():
    """Will test that the shoe has dealt a card. Length of shoe should be 51"""
    deck1 = Shoe()
    deck1.deal_card()
    assert len(deck1.deck) == 51


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
    test_hand.add_card(shoe.deal_card())
    assert test_hand.get_hand_value(shoe) >= 1


def test_hand_value():
    """Test the ability of a hand to calculate its own value"""
    shoe = Shoe()
    test_hand = Hand()
    test_hand.add_card(shoe.deal_card())
    assert test_hand.get_hand_value(shoe) >= 1


def test_hit():
    """tests the ability of the player to add a card to his/her hand"""
    shoe = Shoe()
    test_hand = Hand()
    test_player = Player("Dean")
    test_hand_value = 10
    test_player.hit()
    assert test_hand.get_hand_value(shoe) > test_hand_value
