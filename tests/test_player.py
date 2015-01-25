from player import Player
from hand import Hand
from card import Card
from shoe import Shoe, Clubs, Diamonds, Hearts, Spades

def test_can_hold_hand():
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    player1 = Player("Bob", 20, hand1)
    assert player1.cards == hand1.hand


def test_can_hit():
    shoe1 = Shoe(6)
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    player1 = Player("Juan", 20, hand1)
    player1.hit(shoe1)
    assert len(player1.cards) == 3


def test_can_bet():
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    player1 = Player("Bob", 20, hand1)
    player1.bet(10)
    assert player1.stack == 10
