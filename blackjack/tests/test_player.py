from player import Player
from hand import Hand
from deck import Deck

def test_player_loses_money():
    gordon = Player()
    gordon.lose_money()
    assert gordon.money == 90
    gordon.lose_money()
    assert gordon.money == 80

def test_player_wins_money():
    zach = Player()
    zach.win_money()
    assert zach.money == 110
    zach.win_money()
    assert zach.money == 120

def test_player_wins_extra_money():
    bret = Player()
    bret.win_blackjack()
    assert bret.money == 115
    bret.win_blackjack()
    assert bret.money == 130


def test_player_num_cards():
    zach = Player()
    zach_deck = Deck()
    zach.deal(zach_deck)
    assert zach.num_cards() is 2

def test_player_card_dump():
    bret = Player()
    bret_deck = Deck()
    bret.deal(bret_deck)
    assert bret.num_cards() is 2
    bret.dump_cards()
    assert bret.num_cards() is 0

def test_player_shows_money():
    gordon = Player()
    gordon.win_money()
    gordon_money = gordon.show_money()
    assert gordon_money == "$110"

def test_player_is_broke():
    gordon = Player()
    for i in range(10):
        gordon.lose_money()
    assert gordon.is_broke()
