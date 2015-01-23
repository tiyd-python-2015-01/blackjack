from player import Player

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
