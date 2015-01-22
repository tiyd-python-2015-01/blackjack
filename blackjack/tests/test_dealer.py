from dealer import Dealer
from card import Card
from hand import Hand


def test_dealer_hit():
    hand = Hand([Card("6", "clubs"), Card("5", "hearts")])
    dealer = Dealer()

    dealer.hand = hand

    assert dealer.hit() == True

def test_dealer_does_not_hit():
    hand = Hand([Card("10", "clubs"), Card("7", "hearts")])
    dealer = Dealer()

    dealer.hand = hand

    assert dealer.hit() == False
