from blackjack.hand import Hand
from blackjack.card import Card


seventeen = Hand()
seventeen.add(Card("Queen", "Hearts"))
seventeen.add(Card("7", "Clubs"))
low_ace = Hand()
low_ace.add(Card("Ace", "Spades"))
low_ace.add(Card("Queen", "Clubs"))
low_ace.add(Card("2", "Hearts"))
high_ace = Hand()
high_ace.add(Card("Ace", "Hearts"))
high_ace.add(Card("4", "Spades"))
ace_hand = Hand()
ace_hand.add(Card("Ace", "Hearts"))
ace_hand.add(Card("Ace", "Clubs"))
ace_hand.add(Card("Ace", "Spades"))
ace_hand.add(Card("Ace", "Diamonds"))
blackjack_hand = Hand()
blackjack_hand.add(Card("Ace", "Hearts"))
blackjack_hand.add(Card("King", "Hearts"))
dealer_ace = Hand()
dealer_ace.add(Card("Ace", "Hearts"))
busted_hand = Hand()
busted_hand.add(Card("King", "Hearts"))
busted_hand.add(Card("King", "Hearts"))
busted_hand.add(Card("King", "Hearts"))

def test_hand_class():
    hand = Hand()
    card = Card("8", "Spades")
    hand.add(card)
    assert len(hand) == 1

def test_hand_value():
    assert seventeen.value == 17
    assert low_ace.value == 13
    assert high_ace.value == 15
    assert ace_hand.value == 14

def test_blackjack():
    assert blackjack_hand.blackjack() is True

def test_clear_hand():
    seventeen.clear_hand()
    assert len(seventeen) == 0

def test_ace_in_hand():
    assert dealer_ace.is_ace() is True

def test_is_busted():
    assert busted_hand.check_bust() is True
