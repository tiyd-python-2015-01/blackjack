from dealer import Dealer
from hand import Hand
from card import Card
from deck import Deck, Clubs, Diamonds, Hearts, Spades

def test_can_hold_hand():
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    hand2 = Hand([])
    dealer1 = Dealer(hand1)
    assert dealer1.hand.hand == hand1.hand


def test_can_hit():
    deck1 = Deck()
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    dealer1 = Dealer(hand1)
    dealer1.hit(deck1)
    assert len(dealer1.hand.hand) == 3


def test_play_out_hand():
    deck1 = Deck()
    dealer1 = Dealer()
    dealer1.hand.draw(deck1)
    dealer1.hand.draw(deck1)
    dealer1.play_out_hand(deck1)
    assert dealer1.hand.soft_total > 16 or dealer1.hand.hard_total > 16
