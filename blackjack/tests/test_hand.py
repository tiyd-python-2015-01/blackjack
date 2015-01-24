from hand import Hand
from card import Card


def test_card_list_holds_cards():
    test_cards = []
    test_cards.append(Card("10", "diamonds"))
    test_cards.append(Card("J", "clubs"))

    hand = Hand(10, test_cards)
    assert hand.cards


def test_get_hand_value():
    test_cards = []
    test_cards.append(Card("10", "diamonds"))
    test_cards.append(Card("J", "clubs"))

    hand = Hand(10, test_cards)
    assert hand.get_value() == 20


def test_get_ranks():
    test_cards = []
    test_cards.append(Card("10", "diamonds"))
    test_cards.append(Card("J", "clubs"))

    hand = Hand(10, test_cards)
    assert hand.get_ranks() == ["10", "J"]


def test_ace_detection_and_swap():
    test_cards = []
    test_cards.append(Card("10", "diamonds"))
    test_cards.append(Card("J", "clubs"))
    test_cards.append(Card("A", "hearts"))

    hand = Hand(10, test_cards)
    assert hand.get_value() == 21


def test_two_aces():
    test_cards = []
    test_cards.append(Card("A", "diamonds"))
    test_cards.append(Card("A", "hearts"))

    hand = Hand(10, test_cards)

    assert hand.get_value() == 12


def test_ace_value_incorrect():
    test_cards = []
    test_cards.append(Card("A", "spades"))
    test_cards.append(Card("9", "clubs"))
    test_cards[0].swap_ace()
    hand = Hand(10, test_cards)

    assert hand.get_value() == 20

def test_blackjack():
    test_cards = []
    test_cards.append(Card("A", "spades"))
    test_cards.append(Card("10", "clubs"))
    hand = Hand(10, test_cards)

    assert hand.get_value() == 21
