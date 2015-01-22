from player import Player
from hand import Hand
from card import Card
from deck import Deck, Clubs, Diamonds, Hearts, Spades

def test_can_hold_hand():
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    player1 = Player("Bob", hand1)
    player1.hand = hand1


def test_can_hit():
    deck1 = Deck()
    hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    player1 = Player("Juan", hand1)
    player1.hit(deck1)
    len(player1.hand) == 3
