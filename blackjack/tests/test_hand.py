from hand import Hand
from card import Card
from deck import Deck

spade_of_eights = Card("Spades", "8")
heart_of_eights = Card("Hearts", "8")
a_card = Card("Spades", "4")
a_second_card = Card("Hearts", "5")


def test_hand_grabs():
    my_hand = Hand()
    a_deck = Deck()
    my_hand.grab(a_deck.draw())
    assert len(my_hand) == 1


def test_hand_prints():
    my_hand = Hand()
    my_hand.grab(spade_of_eights)
    my_hand.grab(heart_of_eights)
    target_string = "[S8, H8]"
    hand_string = str(my_hand)
    assert target_string == hand_string


def test_hand_value():
    my_hand = Hand()
    my_hand.grab(a_card)
    my_hand.grab(a_second_card)
    assert my_hand.value() == 9


def test_hand_is_splittable():
    can_split_hand = Hand(spade_of_eights, heart_of_eights)
    can_not_split_hand = Hand(a_card, a_second_card)
    too_big_to_split_hand = Hand(a_card, a_second_card, spade_of_eights)
    assert can_split_hand.can_split()
    assert not can_not_split_hand.can_split()
    assert not too_big_to_split_hand.can_split()
