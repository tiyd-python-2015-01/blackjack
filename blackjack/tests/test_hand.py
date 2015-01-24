from blackjack.hand import Hand
from blackjack.card import Card


first_hand = Hand()
first_hand.add(Card("Queen", "Hearts"))
first_hand.add(Card("7", "Clubs"))
second_hand = Hand()
second_hand.add(Card("Ace", "Spades"))
second_hand.add(Card("Queen", "Clubs"))
second_hand.add(Card("2", "Hearts"))
third_hand = Hand()
third_hand.add(Card("Ace", "Hearts"))
third_hand.add(Card("4", "Spades"))
fourth_hand = Hand()
fourth_hand.add(Card("Ace", "Hearts"))
fourth_hand.add(Card("Ace", "Clubs"))
fourth_hand.add(Card("Ace", "Spades"))
fourth_hand.add(Card("Ace", "Diamonds"))


def test_hand_class():
    hand = Hand()
    card = Card("8", "Spades")
    other_card = Card("8", "Spades")
    hand.add(card)
    assert len(hand) == 1

def test_hand_value():

    assert first_hand.value_check() == 17
    assert second_hand.value_check() == 13
    assert third_hand.value_check() == 15
    assert  fourth_hand.value_check() == 14
