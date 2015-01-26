from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck

spade_of_eights = Card("Spades", "8")
heart_of_eights = Card("Hearts", "8")
a_card = Card("Spades", "4")
a_second_card = Card("Hearts", "5")
an_ace = Card("Diamonds", "1")


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
    seventeen_hand = Hand(spade_of_eights, heart_of_eights, an_ace)
    assert seventeen_hand.value() == 17
    twelve_hand = Hand(an_ace, an_ace)
    assert twelve_hand.value() == 12
    thirteen_hand = Hand(an_ace, an_ace, an_ace)
    assert thirteen_hand.value() == 13
    fourteen_hand = Hand(an_ace, an_ace, an_ace, an_ace)
    assert fourteen_hand.value() == 14
    twenty_hand = Hand(an_ace, an_ace, spade_of_eights)
    assert twenty_hand.value() == 20
    twentyone_hand = Hand(an_ace, an_ace, an_ace, spade_of_eights)
    assert twentyone_hand.value() == 21


def test_has_ace():
    no_ace_hand = Hand(a_card, a_second_card)
    ace_hand = Hand(an_ace, a_card)
    assert not no_ace_hand.has_ace()
    assert ace_hand.has_ace()


def test_hand_is_splittable():
    can_split_hand = Hand(spade_of_eights, heart_of_eights)
    can_not_split_hand = Hand(a_card, a_second_card)
    too_big_to_split_hand = Hand(a_card, a_second_card, spade_of_eights)
    assert can_split_hand.can_split()
    assert not can_not_split_hand.can_split()
    assert not too_big_to_split_hand.can_split()


def test_hand_is_bust():
    busted_hand = Hand(spade_of_eights, heart_of_eights, a_card,
                       a_second_card)
    assert busted_hand.is_bust()


def test_hand_num_cards():
    hand_with_three_cards = Hand(an_ace, a_card, a_second_card)
    assert hand_with_three_cards.num_cards() is 3
