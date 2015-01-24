from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player

def test_make_bet():
    a_player = Player()
    assert a_player.chips == 100
    a_player.make_bet()
    assert a_player.chips == 90

def test_win_bet():
    a_player = Player(chips=90)
    a_player.win_bet()
    assert a_player.chips == 110

def test_win_blackjack():
    a_player = Player(chips=90)
    a_player.win_blackjack()
    assert a_player.chips == 115

def test_push():
    a_player = Player(chips=90)
    a_player.push()
    assert a_player.chips == 100
