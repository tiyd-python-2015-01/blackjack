from dealer import Dealer
from card import Card
from hand import Hand
from game_options import GameOptions
from game import Game


def test_dealer_hit():
    hand = Hand(0, [Card("6", "clubs"), Card("5", "hearts")])
    dealer = Dealer()

    dealer.hand = hand

    assert dealer.hit()


def test_dealer_does_not_hit():
    hand = Hand(0, [Card("10", "clubs"), Card("7", "hearts")])
    dealer = Dealer()

    dealer.hand = hand

    assert not dealer.hit()


def test_dealer_hits_soft_17():
    hand = Hand(0, [Card("6", "clubs"), Card("A", "hearts")])
    dealer = Dealer(hit_soft_17=True)

    dealer.hand = hand

    assert dealer.hit()


def test_dealer_takes_hit():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.dealer.hand = Hand(10, [Card("2", "spades"), Card("J", "clubs")])
    new_game.dealer.takes_hit(new_game.deck.deal())
