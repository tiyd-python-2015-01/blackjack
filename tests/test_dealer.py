from dealer import Dealer
from shoe import Shoe
from hand import Hand
from card import Card
from shoe import Diamonds, Spades


def test_can_hold_hand():
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    dealer1 = Dealer(hand1)
    assert dealer1.hand.hand == hand1.hand


def test_can_hit():
    shoe1 = Shoe(6)
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    dealer1 = Dealer(hand1)
    dealer1.hit(shoe1)
    assert len(dealer1.hand.hand) == 3


def test_play_out_hand():
    shoe1 = Shoe(6)
    dealer1 = Dealer()
    dealer1.hand.draw(shoe1)
    dealer1.hand.draw(shoe1)
    dealer1.play_out_hand(shoe1)
    assert dealer1.hand.soft_total > 16 or dealer1.hand.hard_total > 16
